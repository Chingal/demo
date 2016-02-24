from django.shortcuts import render
from django.views.generic import FormView
from forms import AddProductForm

class AddProductView(FormView):
    template_name = 'ventas/add_product.html'
    form_class    = AddProductForm

    #Si los datos del formalurio son validos, sobreescribos el metodo
    def get_context_data(self, **kwargs):
        context = super(AddProductView, self).get_context_data(**kwargs)
        context['form'] = AddProductForm
        context['info'] = 'Iniciando...'
        return context

    def form_valid(self, form):
        form.save()
        context = self.get_context_data()
        context['info'] = 'Se guardo satisfactoriamente'
        return super(AddProductView, self).form_valid(form)