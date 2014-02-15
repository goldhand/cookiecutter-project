from django.views.generic.base import TemplateView


class BlogView(TemplateView):

    template_name = "blog/list.html"

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        return context
