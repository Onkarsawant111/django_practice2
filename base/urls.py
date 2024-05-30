from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path("home/",views.home, name='home'),
    path("aboutme/", views.aboutme,name="aboutme"),
    path("services/",views.services, name="services"),
    path("contactme/", views.contactme, name="contactme"),
]
