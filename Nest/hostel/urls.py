from django.urls import path
from .views import (HomeView, add_hostel, EditHostel, EditRoom, DeleteHostel, DeleteRoom, HostelDetails)


app_name='hostel'
urlpatterns = [
	path('', HomeView.as_view(), name='home'),
	path('add/hostel/', add_hostel, name='add-hostel'),
	path('edit/hostel/<slug:slug>/', EditHostel.as_view(), name='edit-hostel'),
	path('edit/hostel/room/<int:pk>/', EditRoom.as_view(), name='edit-room'),
	path('delete/hostel/<slug:slug>/', DeleteHostel.as_view(), name='delete-hostel'),
	path('delete/room/<int:pk>/', DeleteRoom.as_view(), name='delete-room'),
	path('hostel/details/<slug:slug>/', HostelDetails.as_view(), name='details')
]