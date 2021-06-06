from django.db import models

# Create your models here.
class detail(models.Model):
    name = models.CharField(max_length=10)
    Id_num = models.BigIntegerField()
    contact = models.BigIntegerField()
    address = models.TextField(blank=True)
   

