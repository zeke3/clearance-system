from django import forms
from accounts.models import User, Student


class UserUpdateForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['username','first_name','last_name','email']



class ProfileUpdateForm(forms.ModelForm):
	course_name = forms.CharField()
	id_number = forms.CharField()

	class Meta:
		model = Student
		fields = ('course_name','id_number')