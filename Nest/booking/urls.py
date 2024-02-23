from django.urls import path
from .views import BookingList, make_booking


app_name = 'booking'
urlpatterns = [
	path('list/', BookingList.as_view(), name='booking'),
	path('place-booking/<slug:slug>/<int:hostel_pk>/<int:room_pk>/', make_booking, name='place-booking'),
]