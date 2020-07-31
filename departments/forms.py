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


class MustSoForm(forms.ModelForm):

	class Meta:
		model = MustSo
		fields = ['student', 'item']


class LaboratoriesForm(forms.ModelForm):

	class Meta:
		model = Laboratories
		fields = ['student', 'item']


class HeadOfDepartmentForm(forms.ModelForm):

	class Meta:
		model = HeadOfDepartment
		fields = ['student', 'item']


class CateringOfficeForm(forms.ModelForm):

	class Meta:
		model = CateringOffice
		fields = ['student', 'item']								


class SportsGamesForm(forms.ModelForm):

	class Meta:
		model = SportsGames
		fields = ['student', 'item']


class AccomodationForm(forms.ModelForm):

	class Meta:
		model = Accomodation
		fields = ['student', 'item']


class AccountsOfficeForm(forms.ModelForm):

	class Meta:
		model = AccountsOffice
		fields = ['student', 'item']

