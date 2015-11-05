from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from .models import *

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

class PlaceCreateView(CreateView):
  model = Place
  template_name = 'place/place_form.html'
  fields = ['category', 'place', 'description']
  success_url = reverse_lazy('question_list')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(PlaceCreateView, self).form_valid(form)
  
class PlaceListView(ListView):
  model = Place
  template_name = 'place/place_list.html'

class PlaceDetailView(DetailView):
  model = Place
  template_name = 'place/place_detail.html'
  