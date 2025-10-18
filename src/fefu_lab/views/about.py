from django.views import generic


class AboutView(generic.TemplateView):
    """Страница 'о нас'."""

    template_name = "fefu_lab/about.html"
