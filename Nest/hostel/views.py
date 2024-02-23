from django.shortcuts import render, reverse, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import AddHostelForm, RoomAddForm
from .models import HostelPicture, Hostel, Room
from django.forms import formset_factory
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required




#default view
class HomeView(ListView):

	model = Hostel
	context_object_name = 'hostels'
	slug_url_kwarg = 'slug'

	template_name = 'hostel/index.html'


@login_required
def add_hostel(request):

	#creating a multiple room forms using the form set factory method
	RoomFormSet = formset_factory(RoomAddForm, extra=5,	max_num=1, absolute_max=100,
			 					validate_max=True, can_delete=True)


	if request.method == 'POST':
		hostel_form = AddHostelForm(request.POST, request.FILES)
		room_forms = RoomFormSet(request.POST)

		if hostel_form.is_valid() and room_forms.is_valid():

			#assigning the user instance to the logged in user
			hostel_form.instance.created_by =request.user

			hostel_form.save()
			
			#proessing each form in the formset and saving data to the database
			for form in room_forms:
				form.instance.hostel = hostel_form.instance
				form.save()

			return redirect('hostel:details', hostel_form.instance.slug)

	else:
		hostel_form = AddHostelForm()
		room_forms = RoomFormSet()

	return render(request, 'hostel/add_hostel.html', {'hostel_form': hostel_form, 'room_forms':room_forms})


class EditHostel(LoginRequiredMixin, UpdateView):

	model = Hostel
	template_name = 'hostel/update_template.html'

	form_class = AddHostelForm

	def get_queryset(self):
		queryset = super().get_queryset()

		return queryset.filter(created_by=self.request.user)


	def get_success_url(self):
		return reverse('hostel:details')



class EditRoom(LoginRequiredMixin, UpdateView):

	model = Room
	template_name = 'hostel/update_template.html'

	fields = [
		'hostel', 'room_type', 'number_available', 'room_capacity', 'cost',
		'simple_description', 'has_half_payment'
	]

	def get_queryset(self):
		queryset = super().get_queryset()

		return queryset.filter(hostel__created_by=self.request.user)


	def get_success_url(self):
		return reverse('hostel:details')



class DeleteHostel(LoginRequiredMixin ,DeleteView):

	model = Hostel
	template_name = 'hostel/delete.html'
	success_url = reverse_lazy('hostel:home')

	def get_queryset(self):
		queryset = super().get_queryset()

		return queryset.filter(created_by=self.request.user)



class DeleteRoom(LoginRequiredMixin, DeleteView):

	model = Room
	template_name = 'hostel/delete.html'
	success_url = reverse_lazy('hostel:home')

	def get_queryset(self):
		queryset = super().get_queryset()

		return queryset.filter(hostel__created_by=self.request.user)



class HostelDetails(DetailView):
	model = Hostel

	slug_url_kwarg = 'slug'
	template_name = 'hostel/details.html'

	context_object_name = 'hostel'

	def get_context_data(self, **kwargs):

		context = super(HostelDetails, self).get_context_data(**kwargs)
		context['rooms'] = context['hostel'].room_set.all()
		context['images'] = context['hostel'].hostelpicture_set.all()

		return context