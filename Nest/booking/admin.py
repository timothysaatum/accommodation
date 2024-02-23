from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
	list_display = ('client', 'hostel', 'school', 'room', 'phone', 'check_in')


admin.site.register(Booking, BookingAdmin)