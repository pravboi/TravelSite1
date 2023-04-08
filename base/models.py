from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    orders = models.ManyToManyField("OrderItem", related_name="orders", blank=True)
    modules = models.ManyToManyField("Module", related_name="modules", blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

class Vehicle(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=5000, null=True)
    recovery_description = models.CharField(max_length=5000, null=True)
    ticket_cost = models.IntegerField(default=0,null=True,blank=True)
    capacity = models.IntegerField(default=0,null=True,blank=True)

class Expedition(models.Model):  # these are the planned expeditions
    name = models.CharField(max_length=100, null=True) # just any mission name
    exp_type = models.CharField(max_length=100, null=True) # suborbital, orbital
    launch_date = models.DateField()
    avalible = models.BooleanField(default=True, null=True, blank=False) 

class CurrentVehicle(models.Model): # these are the current vehicles that are going on a mission
    ship = models.ForeignKey(Vehicle,on_delete=models.SET_NULL,null=True, related_name="ship")  # team that sent invite
    pilots = models.ManyToManyField("User", related_name="pilots", blank=True)
    passengers = models.IntegerField(default=0,null=True,blank=True)
    expedition = models.ForeignKey(Expedition,on_delete=models.SET_NULL,null=True, related_name="expedition")  # team that sent invite

    @property
    def seats_taken(self):
        count = 0
        for p in self.passengers.all():
            count += 1
        return count

class Ticket(models.Model):
    price = models.IntegerField(default=0,null=True,blank=True)
    date_purchased = models.DateField()
    exped = models.ForeignKey(Expedition,on_delete=models.SET_NULL,null=True, related_name="exped")  # team that sent invite

class OrderItem(models.Model):
    tics = models.ManyToManyField("Ticket", related_name="tics", blank=True)
    exp = models.ForeignKey(Expedition,on_delete=models.SET_NULL,null=True, related_name="exp")  # team that sent invite
    vehi = models.ForeignKey(CurrentVehicle,on_delete=models.SET_NULL,null=True, related_name="vehi")  # team that sent invite

    @property
    def get_total_price(self):
        price = 0
        for p in self.tics.all():
            price += p.price
        return price

    @property
    def get_num_tics(self):
        count = 0
        for p in self.tics.all():
            count += 1
        return count


class Question(models.Model):
    mod_name = models.CharField(max_length=100, null=True) 

    prompt = models.CharField(max_length=100, null=True) 

    choice1 = models.CharField(max_length=100, null=True, default="None") 
    choice2 = models.CharField(max_length=100, null=True, default="None") 
    choice3 = models.CharField(max_length=100, null=True, default="None") 
    choice4 = models.CharField(max_length=100, null=True, default="None") 

    answer = models.CharField(max_length=100, null=True, default="None") 

class Module(models.Model):
    max_score = models.FloatField(default=0,null=True,blank=True)
    title = models.CharField(max_length=100, null=True) 
    questions = models.ManyToManyField("Question", related_name="questions", blank=True)


