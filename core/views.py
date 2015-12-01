from django.db.models import Avg
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import PermissionDenied
from .models import *
from .forms import *

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

  def get_context_data(self, **kwargs):
    context = super(PlaceDetailView, self).get_context_data(**kwargs)
    place = Place.objects.get(id=self.kwargs['pk'])
    comments = Comment.objects.filter(place=place)
    context['comments'] = comments
    rating = Comment.objects.filter(place=place).aggregate(Avg('rating'))
    context['rating'] = rating
    return context

class PlaceUpdateView(UpdateView):
  model = Place
  template_name = 'place/place_form.html'
  fields = ['category', 'place', 'description']

  def get_object(self, *args, **kwargs):
    object = super(PlaceUpdateView, self).get_object(*args, **kwargs)
    if object.user != self.request.user:
      raise PermissionDenied()
      return object

class PlaceDeleteView(DeleteView):
  model = Place
  template_name = 'place/place_confirm_delete.html'
  success_url = reverse_lazy('place_list')

  def get_object(self, *args, **kwargs):
    object = super(PlaceDeleteView, self).get_object(*args, **kwargs)
    if object.user != self.request.user:
      raise PermissionDenied()
      return object

class CommentCreateView(CreateView):
  model = Comment
  template_name = 'comment/comment_form.html'
  fields = ['text', 'rating']

  def get_success_url(self):
    return self.object.place.get_absolute_url()

  def form_valid(self, form):
    form.instance.user = self.request.user
    form.instance.place = Place.objects.get(id=self.kwargs['pk'])
    return super(CommentCreateView, self).form_valid(form)

class CommentUpdateView(UpdateView):
  model = Comment
  pk_url_kwarg = 'comment_pk'
  template_name = 'comment/comment_form.html'
  fields = ['text', 'rating']

  def get_success_url(self):
    return self.object.place.get_absolute_url()

  def get_object(self, *args, **kwargs):
    object = super(CommentUpdateView, self).get_object(*args, **kwargs)
    if object.user != self.request.user:
      raise PermissionDenied()
      return object

class CommentDeleteView(DeleteView):
  model = Comment
  pk_url_kwarg = 'comment_pk'
  template_name = 'comment/comment_confirm_delete.html'

  def get_success_url(self):
    return self.object.place.get_absolute_url()

  def get_object(self, *args, **kwargs):
    object = super(CommentDeleteView, self).get_object(*args, **kwargs)
    if object.user != self.request.user:
      raise PermissionDenied()
      return object

class VoteFormView(FormView):
  form_class = VoteForm

  def form_valid(self, form):
    user = self.request.user
    comment = Comment.objects.get(pk=form.data['comment'])
    prev_votes = Vote.objects.filter(user=user, comment=comment)
    has_voted = (prev_votes.count()>0)
    if not has_voted:
      Vote.objects.create(user=user, comment=comment)
    else:
      prev_votes[0].delete()
    return redirect(reverse('place_detail', args=[form.data["place"]]))
  
class UserDetailView(DetailView):
  model = User
  slug_field = 'username'
  template_name = 'user/user_detail.html'
  context_object_name = 'user_in_view'