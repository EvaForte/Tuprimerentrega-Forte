
from django.urls import path

from . import views

urlpatterns = [
   
    path("", views.index, name="index"),
    path("coordinador/list", views.coordinador_list, name="coordinador_list"),
    path("coordinador/form", views.coordinador_form, name="coordinador_form"),
]
