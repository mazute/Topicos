from django.urls import path

from .views import PaginaInicialView, PaginaSobreView, PaginaAjudaView

urlpatterns = [
    path('', PaginaInicialView.as_view(), name='index'),
    path('sobre/', PaginaSobreView.as_view(), name='sobre'),
    path('ajuda/', PaginaAjudaView.as_view(), name='ajuda'),
    
]