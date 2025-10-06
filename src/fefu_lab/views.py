from django.views import generic


class IndexView(generic.TemplateView):
    """Отображение корневой страницы приложения fefu_lab."""

    template_name = "fefu_lab/base.html"
