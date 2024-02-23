from django.db import models
from hostel.models import Hostel, School, Room
from django.contrib.auth import get_user_model
import uuid
import secrets
from django.utils import timezone



user = get_user_model()

SEX = [('Male', 'Male'), ('Female', 'Female')]
class Booking(models.Model):

	client = models.ForeignKey(user, on_delete=models.CASCADE)
	hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
	school = models.ForeignKey(School, on_delete=models.CASCADE)
	room = models.CharField(max_length=30)
	cost = models.FloatField()
	check_in = models.DateField(help_text='YYYY-MM-DD')
	number_of_guests = models.IntegerField()
	phone = models.CharField(max_length=14)
	sex = models.CharField(max_length=10, choices=SEX)
	email_address = models.EmailField()
	uin = models.CharField(max_length=10)
	digital_address = models.CharField(max_length=15)
	receipt = models.CharField(max_length=100)
	date_created = models.DateField(default=timezone.now)
	is_verified = models.BooleanField(default=False)
	slug = models.UUIDField(default=uuid.uuid4, editable=False)
	ref = models.CharField(max_length=100)


	def __str__(self):
		return self.hostel.hostel_name


	def save(self, *args, **kwargs):
		while not self.ref:
			ref = secrets.token_urlsafe(50)
			object_with_similar_ref = Booking.objects.filter(ref=ref)
			if not object_with_similar_ref:
				self.ref = ref

		super().save(*args, **kwargs)