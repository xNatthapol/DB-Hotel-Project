# your_app/urls.py

from django.urls import path
from .views import IndexView, export_table, dynamic_form_view, delete_data

app_name = 'hotel'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('export_table/<str:model_name>', export_table, name='export_table'),
    path('export_table/<str:model_name>/<str:order_by>', export_table, name='export_table'),
    path('export_table/<str:model_name>/<str:order_by>/<str:fields>', export_table, name='export_table'),
    path('delete_data/<str:model_name>/<int:pk>/', delete_data, name='delete_data'),
    path('dynamic-form/', dynamic_form_view, name='dynamic_form_view'),
]
