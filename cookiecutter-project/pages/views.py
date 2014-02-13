from django.shortcuts import render, render_to_response
from django.core.mail import mail_admins
from django.contrib import messages
from django.template import RequestContext
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.views.generic.base import TemplateView

from .forms import ContactForm


class PageView(TemplateView):

    template_name = "404.html"

    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        context['contact_form'] = ContactForm()
        return context


def contact(request):
    form = ContactForm()
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = '{} from {}'.format(form.cleaned_data['feedback'], email)
            subject = unicode('Feedback: {}').format(subject)
            mail_admins(subject, message)
            _next = request.POST.get('next')
            messages.success(request, 'Thanks for the feedback!')
            if _next:
                return HttpResponseRedirect(_next)

    _next = ""
    if request.GET.get('next'):
        _next = request.GET.get('next')

    context = {'form': form, 'next': _next}
    return render_to_response('pages/contact.html',
                              context,
                              context_instance=RequestContext(request))