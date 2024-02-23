from django.shortcuts import render,redirect
from django.views.generic import ListView, CreateView
from .models import Booking
from .forms import BookingForm
from hostel.models import Hostel, Room




class BookingList(ListView):

	model = Booking
	template_name = 'booking/booking_list.html'
	context_object_name = 'bookings'
	slug_kwargs_url = 'slug'


def make_booking(request, slug, hostel_pk, room_pk):

	hostel = Hostel.objects.get(pk=hostel_pk)
	room = Room.objects.get(pk=room_pk)
	room_nums = room.room_numbers()
	
	if request.method == 'POST':
		form = BookingForm(request.POST)

		if form.is_valid():


			school = form.cleaned_data['school']
			cost = room.cost
			check_in = form.cleaned_data['check_in']
			number_of_guests = form.cleaned_data['number_of_guests']
			phone = form.cleaned_data['phone']
			email_address = form.cleaned_data['email_address']
			uin = form.cleaned_data['uin']
			digital_address = form.cleaned_data['digital_address']
			sex = form.cleaned_data['sex']

			if Booking.objects.all().count() == 0:
				
				Booking.objects.create(client=request.user, hostel=hostel, school=school, room=room.room_type, cost=cost, 
					check_in=check_in, number_of_guests=number_of_guests, phone=phone, sex=sex, email_address=email_address,
					 uin=uin, digital_address=digital_address)
				form.send_email()

				room_nums['Room1']['has_occupant'] = True
				room_nums['Room1']['capacity'] -= 1
				room_nums['Room1']['sex'] = sex
				print(room_nums)

			return redirect('hostel:home')

	form = BookingForm()

	return render(request, 'booking/booking.html', {'form': form})
