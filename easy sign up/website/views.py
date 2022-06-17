from django.shortcuts import reverse
from django.views import generic
from .form import *

class Home(generic.TemplateView):
    template_name = 'index.html'

class Succes(generic.TemplateView):
    template_name = 'succes.html'
    
class Registration(generic.CreateView):
    template_name = 'signup.html'
    form_class = Easy
    
    def get_success_url(self):
        return reverse('django:succes')
