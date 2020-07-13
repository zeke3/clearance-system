from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth import get_user_model
from .models import User, Student
#User = get_user_model()

class TeacherSignupForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = User
		
	def save(self,commit=True):
		user = super().save(commit=False)
		user.is_teacher = True
		if commit:
			user.save()
		return user		


class StudentSignupForm(UserCreationForm):

	class Meta(UserCreationForm.Meta):
		model = User
		fields = ['username','first_name','last_name','email']

	@transaction.atomic
	def save(self, **kwargs):
		user = super().save(commit=False)
		user.is_student = True
		user.save()
		# student = Student.objects.create(user=user)
		return user


class StudentProfileForm(forms.ModelForm):
	course_name = forms.CharField(max_length=150)
	id_number = forms.CharField(max_length=15)

	class Meta(forms.ModelForm):
		model = Student
		fields = ('course_name','id_number')


class LoginForm(forms.Form):
	username = forms.CharField(max_length=150)
	password = forms.CharField(widget=forms.PasswordInput())

