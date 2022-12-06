from django.db import models


# Create your models here.
class Customer(models.Model):
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.f_name + ' ' + self.l_name
