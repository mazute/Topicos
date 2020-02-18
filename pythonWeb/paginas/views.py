from django.views.generic import TemplateView


class PaginaInicialView(TemplateView):
    template_name = 'paginas/index.html'


class PaginaSobreView(TemplateView):
    template_name = 'paginas/sobre.html'


class PaginaAjudaView(TemplateView):
    template_name = 'paginas/ajuda.html'
