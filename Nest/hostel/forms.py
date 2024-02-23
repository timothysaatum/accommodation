from django import forms
from .models import Hostel, Room, HostelPicture


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result



class AddHostelForm(forms.ModelForm):

	upload_hostel_pictures = MultipleFileField()

	class Meta:
		model = Hostel
		exclude = ('created_by', 'date_added', 'modified_on', 'slug')



	def _save_m2m(self):

		super()._save_m2m()

		#Creating hostel images
		hostel_pics = [
			HostelPicture(hostel=self.instance, image=file) for file in self.files.getlist('upload_hostel_pictures')
		]

		HostelPicture.objects.bulk_create(hostel_pics)


class RoomAddForm(forms.ModelForm):


	class Meta:
		model = Room
		exclude = ('occupant_sex', 'has_occupant', 'hostel')

