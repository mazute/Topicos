from django.views.generic import TemplateView


class PaginaInicialView(TemplateView):
    template_name = 'paginas/index.html'
