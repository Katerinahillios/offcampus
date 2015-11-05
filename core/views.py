from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import *

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

class PlaceCreateView(CreateView):
  model = Place
  template_name = 'place/place_form.html'
  fields = ['category', 'place', 'description']
  success_url = reverse_lazy('place_list')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(PlaceCreateView, self).form_valid(form)

class PlaceListView(ListView):
  model = Place
  template_name = 'place/place_list.html'

class PlaceDetailView(DetailView):
  model = Place
  template_name = 'place/place_detail.html'

class PlaceUpdateView(UpdateView):
  model = Place
  template_name = 'place/place_form.html'
  fields = ['category', 'place', 'description']

class PlaceDeleteView(DeleteView):
  model = Place
  template_name = 'place/place_confirm_delete.html'
  success_url = reverse_lazy('place_list')

class CommentCreateView(CreateView):
  model = Comment
  template_name = 'comment/comment_form.html'
  fields = ['text']

  def get_success_url(self):
    return self.object.place.get_absolute_url()

  def form_valid(self, form):
    form.instance.user = self.request.user
    form.instance.place = Place.objects.get(id=self.kwargs['pk'])
    return super(CommentCreateView, self).form_valid(form)