from django.urls import path
from . import views

urlpatterns = [
    path('uses', views.uses ),
    path('pictures', views.pictures ),
    path('formdata', views.formdata , name='formdata')
]