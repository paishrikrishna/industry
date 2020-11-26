from .models import login_model
from django import forms

class login_form(forms.ModelForm):
	class Meta:
		model = login_model
		fields={
			'username',
			'password',
			'mobile_no',
			'auth',
			'session_key'
		}