from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home.html', views.home),
    path('aboutme.html', views.aboutme),
    path('contactme.html', views.contactme),
    path('services.html', views.services),
]