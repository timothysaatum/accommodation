from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model
import uuid



user = get_user_model()
#
class School(models.Model):

	name = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	region = models.CharField(max_length=50)
	school_gps_coordinates = models.CharField(max_length=150)
	date_added = models.DateTimeField(default=timezone.now)
	slug = models.UUIDField(default=uuid.uuid4, editable=False)

	def __str__(self):
		return self.name


	def get_absolute_url(self):
		return reverse('hostel:school-details', kwargs={'pk':self.slug})

	#splits the school gps points and return only the latitude point
	def get_school_latitude(self):

		lat, _ = self.school_gps_coordinates.split(',')

		return float(lat)

	#splits the school gps point and return only the longitude point
	def get_school_longitude(self):

		_, lng = self.school_gps_coordinates.split(',')

		return float(lng)


class Amenities(models.Model):

	amenity_name = models.CharField(max_length=100)
	icon = models.CharField(max_length=100)

	def __str__(self):
		return self.amenity_name


	class Meta:
		verbose_name_plural = 'Amenities'




class Hostel(models.Model):

	school_located = models.ForeignKey(School, on_delete=models.CASCADE)
	created_by = models.ForeignKey(user, on_delete=models.CASCADE)
	campus_of_location = models.CharField(max_length=100)
	hostel_name = models.CharField(max_length=100)
	hostel_contact = models.CharField(max_length=13)
	number_of_rooms = models.PositiveIntegerField()
	duration_of_rent = models.PositiveIntegerField()
	rating = models.DecimalField(max_digits=10, decimal_places=1)
	display_image = models.ImageField(upload_to='hostel/display/images')
	hostel_gps_coordinates = models.CharField(max_length=100)
	amenities = models.ManyToManyField(Amenities)
	account_number = models.PositiveIntegerField()
	account_name = models.CharField(max_length=100)
	date_added = models.DateTimeField(auto_now_add=True)
	modified_on = models.DateTimeField(auto_now=True)
	slug = models.UUIDField(default=uuid.uuid4, editable=False)
	publish = models.BooleanField(default=False)

	def __str__(self):
		return self.hostel_name



	def get_hostel_lat(self):
		x, _ = self.hostel_gps_coordinates.split(',')

		return float(x)


	def get_hostel_lng(self):
		_, y = self.hostel_gps_coordinates.split(',')

		return float(y)


	def get_absolute_url(self):

		return reverse('hostel:hostel-details', kwargs={'slug':self.slug})


	def get_school_of_location(self):
		return self.school_located.name


	def calculate_distance(self):
		pass


class HostelPicture(models.Model):
	hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
	image = models.FileField(upload_to='hostels/images')


	def __str__(self):
		return self.hostel.hostel_name



class Room(models.Model):

	hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
	room_type = models.CharField(max_length=100)
	number_available = models.PositiveIntegerField()
	room_capacity = models.PositiveIntegerField()
	cost = models.FloatField()
	simple_description = models.TextField(blank=True, null=True)
	occupant_sex = models.CharField(max_length=15, blank=True, null=True)
	has_occupant = models.BooleanField(default=False)
	has_half_payment = models.BooleanField(default=False)
	is_full = models.BooleanField(default=False)


	def __str__(self):
		return self.room_type


	def room_numbers(self):

		rooms = {'Room'+str(room):{'capacity':self.room_capacity, 'sex':None, 'has_occupant':None} for room in range(1, (self.number_available + 1))}

		return rooms


	def vacant_rooms(self):

		for num in range(1, (self.number_available + 1)):
			if self.room_numbers()['Room'+str(num)]['capacity'] == 0:
				pass


	def cost_per_bed(self):

		cost_per_heard = int(self.cost) / self.room_capacity

		return cost_per_heard


	def get_room_gender(self):

		room = Room.objects.get(pk=self.pk)

		return room.occupant_sex

	def vacancy_remaining(self):
		pass


	def pay_installment(self):

		if self.has_half_payment == True:

			half_payment = self.cost_per_bed() / 2

			return half_payment

		return 'No installment allowed'
