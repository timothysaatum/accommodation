from django.shortcuts import render, reverse
from django.views.generic import TemplateView, CreateView
from .forms import AddHostelForm, RoomAddForm
from django.forms import formset_factory



class HomeView(TemplateView):
	template_name = 'hostel/index.html'



def add_hostel(request):
	
	if request.method == 'POST':
		hostel_form = AddHostelForm(request.POST)
		room_form = RoomAddForm(request.POST)

		if hostel_form.is_valid() and room_form.is_valid():
			hostel_form.created_by =request.user

			hostel_form.save()
			room_form.save()
			return redirect('hostel:home')

	else:
		hostel_form = AddHostelForm()
		RoomFormSet = formset_factory(
			 			RoomAddForm, extra=5, 
			 			max_num=1, absolute_max=100,
			 			validate_max=True,
			 			can_delete=True
			 			)
		room_form = RoomFormSet()

	return render(request, 'hostel/add_hostel.html', {'hostel_form': hostel_form, 'room_form':room_form})