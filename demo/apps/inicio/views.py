from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import FormView
from forms import ContactForm

class ContactView(FormView):
    form_class    = ContactForm
    template_name = 'inicio/contact.html'
    success_url   = reverse_lazy('contact')

    def get_context_data(self, **kwargs):
        ctx           = super(ContactView, self).get_context_data(**kwargs) #Obtenemos el contexto del form
        ctx['enviar'] = False
        return ctx

    def form_valid(self, form):
        txtEmail = form.cleaned_data['email']
        txtTexto = form.cleaned_data['texto']

        form.send_email( txtEmail,txtTexto )
        return super(ContactView, self).form_valid(form)
