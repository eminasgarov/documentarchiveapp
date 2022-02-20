from django.urls import path
from . import views

urlpatterns = [
    path('', views.documents, name='documents'),
    path('type/<slug:document_type_slug>/', views.documents, name='documents_by_type'),
    path('search/', views.search, name='search')
]