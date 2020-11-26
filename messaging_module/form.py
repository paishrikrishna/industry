from .models import messages_model
from django import forms

class messages_form(forms.ModelForm):
	class Meta:
		model = messages_model
		fields={
			'sender',
			'rx',
			'message',
			'date',
			'time'
		}