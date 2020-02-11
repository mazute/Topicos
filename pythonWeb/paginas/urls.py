from django.urls import path
from .views import PaginaInicialView

urlpatterns = [
    path('inicio/', PaginaInicialView.as_view(), name='index'),
]