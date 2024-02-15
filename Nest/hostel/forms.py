from django import forms
from .models import Hostel, Room


class AddHostelForm(forms.ModelForm):

	class Meta:
		model = Hostel
		exclude = ('created_by', 'date_added', 'modified_on', 'slug')


class RoomAddForm(forms.ModelForm):


	class Meta:
		model = Room
		exclude = ('occupant_sex', 'has_occupant')
