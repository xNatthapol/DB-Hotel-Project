from django.urls import path
from django.views.generic import RedirectView

from .views import export_table, IndexView

app_name = 'hotel'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('export_table/<str:model_name>/<str:order_by>', export_table, name='export_table'),
]
