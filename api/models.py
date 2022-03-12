from django.db import models

# Create your models here.
class Countries(models.Model):
  id = models.AutoField(primary_key = True)
  name = models.CharField(max_length = 50, blank = False, default='')
  capital = models.CharField(max_length = 50, blank = False, default = '')
  
  class Meta:
    ordering = ('id',)