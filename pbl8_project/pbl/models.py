from django.db import models
from django.template.defaultfilters import slugify

import datetime
YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))

# Create your models here.
class Treatment(models.Model):
  name = models.CharField(max_length=100)
  slug = models.SlugField()
  description = models.TextField()
  studies_for = models.ManyToManyField('Study', blank=True, related_name="studies_for+")
  studies_against = models.ManyToManyField('Study', blank=True, related_name="studies_against+")
  def save(self, *args, **kwargs):
    if not self.id:
      # Newly created object, so set slug
      self.slug = slugify(self.name)

      super(Treatment, self).save(*args, **kwargs)
  def __str__(self):              # __unicode__ on Python 2
    return self.name
  class Meta:
    ordering = ('name',)

class Study(models.Model):
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  journal = models.CharField(max_length=200)
  year = models.IntegerField('year', max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
  funder = models.CharField(max_length=200, blank=True)
  def __str__(self):              # __unicode__ on Python 2
    return self.title
  class Meta:
    ordering = ('title',)