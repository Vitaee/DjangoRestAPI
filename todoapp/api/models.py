from django.db import models
from django.utils import timezone
# Create your models here.

class Task(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField(null=False , blank=True)
  completed = models.BooleanField(default=False, blank=True, null=True)
  regisDate = models.DateTimeField(default=timezone.now,verbose_name="Regis Date")
      
  def __str__(self):
    return self.title