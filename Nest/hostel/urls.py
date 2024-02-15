from django.urls import path
from .views import (HomeView, add_hostel)


app_name='hostel'
urlpatterns = [
	path('homePage/viewList/', HomeView.as_view(), name='home'),
	path('add/hostel/', add_hostel, name='add-hostel')
]