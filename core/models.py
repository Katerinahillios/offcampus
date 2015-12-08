import os
import uuid

def upload_to_location(instance, filename):
  blocks = filename.split('.')
  ext = blocks[-1]
  filename = "%s.%s" % (uuid.uuid4(), ext)
  instance.title = blocks[0]
  return os.path.join('uploads/', filename)

RATING_CHOICES = (
  (0, 'None'),
  (1, '*'),
  (2, '**'),
  (3, '***'),
  (4, '****'),
  (5, '*****'),
)

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

category_options = (
(0, 'Select...'),
(1, 'Fall Festivities'),
(2, 'Winter Festivities'),
(3, 'Spring Festivities'),
(4, 'Bite To Eat'),
(5, 'Night Life'),
(6, 'Girls Night Out'),
(7, 'Date Night'),
)

# Create your models here.
class Place(models.Model):
  category = models.IntegerField(choices=category_options, default=0)
  place = models.CharField(max_length=300, default="")
  location = models.CharField(max_length=300, default="")
  description = models.TextField(null=True, blank=True, default="")
  created_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User)
  rating = models.IntegerField(choices=RATING_CHOICES, default=0)
  image_file = models.ImageField(upload_to=upload_to_location, null=True, blank=True)

  def __unicode__(self):
    return self.place

  def get_absolute_url(self):
    return reverse("place_detail", args=[self.id])

class Comment(models.Model):
  place = models.ForeignKey(Place)
  user = models.ForeignKey(User)
  created_at = models.DateTimeField(auto_now_add=True)
  text = models.TextField()
  rating = models.IntegerField(choices=RATING_CHOICES, default=0)

  def __unicode__(self):
    return self.text

class Vote(models.Model):
  user = models.ForeignKey(User)
  comment = models.ForeignKey(Comment, blank=True, null=True)

  def __unicode__(self):
    return "%s upvoted" % (self.user.username)