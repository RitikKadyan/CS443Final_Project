from django.db import models


# Create your models here.
class Customer(models.Model):
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    username = models.CharField(max_length=100, default='test')
    password = models.CharField(max_length=100, default='test')
    age = models.IntegerField()

    def __str__(self):
        return self.f_name + ' ' + self.l_name


class Game_studio(models.Model):
    num_of_games_released = models.IntegerField()
    studio_name = models.CharField(max_length=20)


class Games(models.Model):
    g_name = models.CharField(max_length=20)
    g_qty_sold = models.IntegerField()
    gs_id = models.ForeignKey(Game_studio, on_delete=models.CASCADE)


class Game_Info(models.Model):
    choices_ = []
    games = Games.objects.all()
    for g in games:
        choices_.append([g.id, g.g_name])
    Games = models.CharField(max_length=20, blank=True, choices=choices_)


# In-App Purchases
class IAP(models.Model):
    iap_name = models.CharField(max_length=20)
    iap_cost = models.IntegerField()
    g_id = models.ForeignKey(Games, on_delete=models.CASCADE)


class Transaction(models.Model):
    c_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    g_id = models.ForeignKey(Games, on_delete=models.CASCADE)
    iap_id = models.ForeignKey(IAP, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.c_id) + ' ' + str(self.g_id)


class Employee(models.Model):
    emp_first_name = models.CharField(max_length=20)
    emp_last_name = models.CharField(max_length=20)
    emp_pay = models.IntegerField()
