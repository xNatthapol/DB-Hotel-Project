from django.urls import path
from django.views.generic import RedirectView

from .views import export_table, IndexView, delete_data

app_name = 'hotel'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('export_table/<str:model_name>', export_table, name='export_table'),
    path('export_table/<str:model_name>/<str:order_by>', export_table, name='export_table'),
    path('export_table/<str:model_name>/<str:order_by>/<str:fields>', export_table, name='export_table'),
    path('delete_data/<str:model_name>/<int:pk>/', delete_data, name='delete_data'),
]
