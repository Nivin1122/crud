from django.db import models

# Create your models here.
class Coaches(models.Model):
    img = models.ImageField(upload_to="images")
    coach_name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.coach_name


class Players(models.Model):
    player_name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="images")
    coach_name = models.ForeignKey(Coaches,on_delete=models.CASCADE)
    description = models.TextField(null=True)

    def __str__(self):
        return self.player_name


class Booking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    coach_name = models.ForeignKey(Coaches,on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)


    def __str__(self):
        return self.name