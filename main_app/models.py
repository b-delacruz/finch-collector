from django.db import models
from django.urls import reverse

class Finch(models.Model):
  name = models.CharField(max_length=100)
  age = models.IntegerField()

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('finches_detail', kwargs={'finch_id': self.id})