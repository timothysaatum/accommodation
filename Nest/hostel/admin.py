from django.contrib import admin
from .models import Hostel, Amenities, Room, School, HostelPicture


class SchoolAdmin(admin.ModelAdmin):
	list_display = ('name', 'city', 'region', 'school_gps_coordinates', 'date_added')



class HostelAdmin(admin.ModelAdmin):
	list_display = ('school_located', 'created_by', 'hostel_name', 'campus_of_location', 'hostel_contact', 'slug')


class AmenityAdmin(admin.ModelAdmin):
	list_display = ('amenity_name', 'icon')


class RoomAdmin(admin.ModelAdmin):
	list_display = ('hostel', 'room_type', 'number_available', 'cost', 'room_numbers')


class HostelPictureAdmin(admin.ModelAdmin):
	list_display = ('hostel', 'image')


admin.site.register(School, SchoolAdmin)
admin.site.register(Hostel, HostelAdmin)
admin.site.register(Amenities, AmenityAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(HostelPicture, HostelPictureAdmin)
