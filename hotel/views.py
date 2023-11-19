from django.shortcuts import render, redirect
from django.apps import apps
from django.views import View


def export_table(request, app_name, model_name, fields=None):
    # table = request.GET.get('search')
    model = apps.get_model(app_label=app_name, model_name=model_name)
    
    if fields is None:
        fields = [field.name for field in model._meta.get_fields() if not field.is_relation]

    data = model.objects.values(*fields)  # Retrieve only the specified fields
    return render(request, 'export_table.html', {'data': data, 'fields': fields})

# class TableExportView(View):
#     template_name = 'export_table.html'
#
#     def get(self, request, app_name, model_name, fields=None):
#         return export_table(request, app_name, model_name, fields)
#
#     def post(self, request, app_name, model_name, fields=None):
#         return export_table(request, app_name, model_name, fields)


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        # selected_model = request.GET.get('search')
        # if selected_model:
        #     return redirect('hotel:export_table', app_name='hotel', model_name=selected_model)
        models = apps.get_models()
        model_names = [model.__name__ for model in models][:-6]
        content = {
            'options': model_names,
        }
        return render(request, self.template_name, content)

    def post(self, request):
        selected_model = request.POST.get('search')
        return redirect('hotel:export_table', app_name="hotel", model_name=selected_model)
