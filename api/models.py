from django.db import models

# Create your models here.
class Countries(models.Model):
  id = models.AutoField(primary_key = True)
  name = models.CharField(max_length = 50, blank = False, default='')
  capital = models.CharField(max_length = 50, blank = False, default = '')

  def __str__(self):
      return str(self.id)+') '+self.name

  class Meta:
    ordering = ('id',)
