from django.db import models

# Create your models here.

class Booking(models.Model):
	name = models.CharField(max_length=100)
	phone_no = models.CharField(max_length=20)
	email = models.EmailField(max_length=100)

	def __str__(self):
		return str(self.name)

class Payment(models.Model):
	fair_amount = models.FloatField()
	booking = models.OneToOneField(Booking)

