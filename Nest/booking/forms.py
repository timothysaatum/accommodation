from django import forms
from .models import Booking
from django.conf import settings
from django.core.mail import send_mail



class BookingForm(forms.ModelForm):

	
	def send_email(self):
		from_mail = settings.EMAIL_HOST_USER
		to_mail = [self.cleaned_data['email_address']]


		subject = 'Booking was successful'

		body = 'Your room has been reserved successfully, thank you for using our service'
		try:
			send_mail(subject, body, from_mail, to_mail)
		except Exception as e:
			print(e)

	class Meta:
		model = Booking
		exclude = ('client', 'receipt', 'date_created', 'is_verified', 'slug', 'ref', 'hostel', 'room', 'cost')

		widgets = {
            'check_in': forms.widgets.DateInput(attrs={'type': 'date'})
        }