from django.shortcuts import render, redirect
from django.apps import apps
from django.views import View

APP_NAME = 'hotel'
filter_explanations = {
        'equal': 'iexact',
        'have': 'icontains',
        'is greater than': 'gt',
        'is less than': 'lt',
        'is greater than or equal to': 'gte',
        'is less than or equal to': 'lte',
    }

def convert_to_code(explanation):
    return filter_explanations[explanation]

def convert_code_to_filter(atrribute: str, code: str, value, where: dict):
    try :
        value = int(value)
    except ValueError:
        value = value

    where[f'{atrribute}__{code}'] = value
    return where



def export_table(request, model_name, fields=None, order_by=None):
    search = request.session.get('search', '')
    order = request.session.get('order_by', '')
    selected = request.session.get('selected', '')
    model = apps.get_model(app_label="hotel", model_name=model_name)
    models = apps.get_models()
    model_names = [mo.__name__ for mo in models][:-6]

    all_fil = [field.name for field in model._meta.get_fields() if
              not field.is_relation]
    if fields is None:
        fields = all_fil
    else:
        if len(fields) == 1:
            fields = fields[0]
        else:
            fields = fields.split(',')

    data = model.objects.order_by(order).values(*fields)

    content = {
        'options': model_names,
        'data': data,
        'fields': all_fil,
        'fields_table': fields,
        'search': search,
        'order_by': order,
        'selected': selected,

    }
    return render(request, 'export_table.html', content)

def perform_where(models: list, where: list, fields: list):
    if len(models) == 1:
        return models[0].objects.filter(**where).values(*fields)

def get_relation_details(model):
    relation_details = []

    for field in model._meta.get_fields():
        if field.is_relation:
            related_model = field.related_model
            relation_detail = {
                'name': field.name,
                'related_model': related_model.__name__,
                'related_app_label': related_model._meta.app_label,
            }
            relation_details.append(relation_detail)

    return relation_details


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):

        models = apps.get_models()
        model_names = [model.__name__ for model in models][:-6]
        content = {
            'options': model_names,
            'fields': ['id'],
        }


        return render(request, self.template_name, content)

    def post(self, request):
        selected_model = request.POST.get('search')
        order_by = request.POST.get('order_by')
        selected = request.POST.get('selected')
        list_selected = request.POST.getlist('fields')

        request.session['search'] = selected_model
        request.session['order_by'] = order_by
        request.session['selected'] = selected

        if selected == 'HIGH->LOW' and order_by != 'None':
            order_by = '-' + order_by
        if list_selected:
            string = list_selected[0]
            for field in list_selected[1::]:
                string += ',' + field
                print(string)
            return redirect('hotel:export_table', model_name=selected_model, order_by=order_by, fields=string)


        return redirect('hotel:export_table', model_name=selected_model, order_by=order_by)
