from django.urls import path
from django.views.generic import RedirectView

from .views import export_table, IndexView

app_name = 'hotel'
urlpatterns = [
    path('export_table/<str:app_name>/<str:model_name>/', export_table, name='export_table'),
    path('export_table/<str:app_name>/<str:model_name>/<str:fields>/', export_table, name='export_table_with_fields'),
    path("", IndexView.as_view(), name='index'),
]
