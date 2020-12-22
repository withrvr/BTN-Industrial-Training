from django import forms
from .models import ContactModels


class ContactForm(forms.ModelForm):
	name = forms.CharField(
		required=True,
		widget=forms.TextInput(
			attrs={
				"placeholder": "Your Name Please",
				"class": "form-control",
			}
		)
	)
	email = forms.EmailField(
		required=True,
		widget=forms.EmailInput(
			attrs={
				"placeholder": "Your Email Please",
				"class": "form-control",
			}
		)
	)
	message = forms.CharField(
		required=True,
		widget=forms.Textarea(
			attrs={
				"placeholder": "Please Enter your Message",
				"class": "form-control",
			}
		)
	)

	class Meta:
		model = ContactModels
		fields = [
			'name',
			'email',
			'message'
		]


