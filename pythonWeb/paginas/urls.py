from django.urls import path

from .views import PaginaInicialView, PaginaSobreView

urlpatterns = [
    path('', PaginaInicialView.as_view(), name='index'),
    path('sobre/', PaginaSobreView.as_view(), name='sobre'),
    
]