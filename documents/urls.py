from django.urls import path
from . import views

urlpatterns = [
    path('', views.procedures, name='procedures'),
    path('procedures', views.procedures, name='procedures'),
    path('procedure_search', views.procedure_search, name='procedure_search'),
]