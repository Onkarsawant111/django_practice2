from django.urls import path
from . import views

urlpatterns = [
    path('uses', views.uses ),
]