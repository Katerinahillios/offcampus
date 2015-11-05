from django.db import models
from django.contrib.auth.models import User

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
  description = models.TextField(null=True, blank=True, default="")
  created_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User)

  def __unicode__(self):
    return self.place


