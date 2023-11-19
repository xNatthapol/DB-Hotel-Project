from django.shortcuts import render, redirect
from django.apps import apps

def export_table(request, app_name, model_name, fields=None):
    # table = request.GET.get('search')
    model = apps.get_model(app_label=app_name, model_name=model_name)
    
    if fields is None:
        fields = [field.name for field in model._meta.get_fields() if not field.is_relation]

    data = model.objects.values(*fields)  # Retrieve only the specified fields
    return render(request, 'export_table.html', {'data': data, 'fields': fields})


def redirect_to_export_table(request, *args, **kwargs):
    app_name = kwargs.get('app_name', 'hotel')
    model_name = kwargs.get('model_name', 'Employee')
    
    return redirect('hotel:export_table', app_name=app_name, model_name=model_name)

def your_view(request):
    # Get all models in the app
    models = apps.get_models()

    # Extract model names
    model_names = [model.__name__ for model in models]

    return render(request, 'index.html', {'options': model_names})
