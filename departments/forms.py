from django import forms


class UploadForm(forms.Form):
	student = forms.CharField()
	item = forms.CharField()