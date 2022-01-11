from django.urls import path
from . import views

urlpatterns = [
    path('', views.kis_documents, name='kis_documents'),
    path('kis_documents/<slug:document_type_slug>/', views.kis_documents, name='documents_by_type'),
    path('search/', views.search, name='search')

]