from django.shortcuts import render, redirect
from django.apps import apps
from django.views import View


def export_table(request, model_name, fields=None):
    # table = request.GET.get('search')
    model = apps.get_model(app_label="hotel", model_name=model_name)
    models = apps.get_models()
    model_names = [model.__name__ for model in models][:-6]

    if fields is None:
        fields = [field.name for field in model._meta.get_fields() if not field.is_relation]

    data = model.objects.values(*fields)  # Retrieve only the specified fields
    content = {
        'options': model_names,
        'data': data,
        'fields': fields,
    }
    return render(request, 'export_table.html', content)

# def details_view(request, app_name, model_name, pk):




class IndexView(View):
    template_name = 'index.html'

    def get(self, request):

        models = apps.get_models()
        model_names = [model.__name__ for model in models][:-6]
        content = {
            'options': model_names,
        }
        return render(request, self.template_name, content)

    def post(self, request):
        selected_model = request.POST.get('search')
        return redirect('hotel:export_table', model_name=selected_model)
