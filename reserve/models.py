from django.db import models
from django.contrib.auth.models import User

class hotel(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=10000)
    address = models.TextField()
    rank = models.CharField(max_length=100)

    def __str__(self):
        return "%s" %(self.name)

class reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(hotel,on_delete=models.CASCADE)
    party = models.IntegerField()
    startday = models.DateField()
    days = models.IntegerField()
    date = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self):
        return "[%s] %s" %(self.user, self.hotel)




