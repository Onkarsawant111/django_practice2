from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path("about-me/", views.aboutme, name="aboutme"),
    path("services/",views.services, name="services"),
    path("contact-me/", views.contactme, name="contactme"),
    path("form/", views.form, name='form'),
    path("thankyou/", views.thankyou, name='thankyou'),
    path("submit/", views.submit, name='submit')
]
