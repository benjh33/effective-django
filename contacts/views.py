from django.shortcuts import render, redirect, RequestContext
from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView 
from django.http import JsonResponse
from crispy_forms.utils import render_crispy_form

from .models import Contact
from .forms import ContactForm

from jsonview.decorators import json_view


class AjaxResponseMixin(object):
    """
    handles ajax form data to and from form CBVs. If the request is ajax,
    returns a JSON object w/ success and errors or an empty form if successful.
    """
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            data = dict((('form_errors', form.errors), ('success', False)))
            return JsonResponse(data, status=200)
        else:
            return response

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = dict((('form_html', render_crispy_form(ContactForm, 
                context=RequestContext(self.request))), 
                    ('success', True)))
            return JsonResponse(data, status=200)
        else:
            return response

class ContactView(AjaxResponseMixin, ListView):
    template_name = 'base.html'
    model = Contact
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context


class CreateContactView(AjaxResponseMixin, CreateView):

    form_class = ContactForm
    model = Contact
    template_name = 'create_contact.html'

    def get_success_url(self):
        return reverse('create-contact')

