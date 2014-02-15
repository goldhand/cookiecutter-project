from django.shortcuts import render, render_to_response
from django.core.mail import mail_admins
from django.contrib import messages
from django.template import RequestContext
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.views.generic.base import TemplateView


class BlogView(TemplateView):

    template_name = "blog/list.html"

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        return context
