from django import forms
from .models import *

class LibraryForm(forms.ModelForm):

	class Meta:
		model = Library
		fields = ['student','item']


class WorkshopForm(forms.ModelForm):

	class Meta:
		model = Workshop
		fields = ['student', 'item']