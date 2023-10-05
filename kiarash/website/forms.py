from django import forms

# Create your forms here.

class ContactForm(forms.Form):
	name = forms.CharField(max_length = 255)
	subject = forms.CharField(max_length = 255)
	email_address = forms.EmailField(max_length = 255)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)