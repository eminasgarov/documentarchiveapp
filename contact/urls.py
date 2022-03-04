from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('request/', views.access_request, name='access_request'),
]