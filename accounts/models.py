from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.utils import timezone




class User(AbstractUser):
	is_student = models.BooleanField(default=False)
	is_teacher = models.BooleanField(default=False)
	

class Student(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
	course_name = models.CharField(max_length=100)
	id_number = models.CharField(max_length=15)


	# def get_absolute_url(self):
	# 	return reverse('accounts:phme', args=[self.id])


	def __str__(self):
		return f"{self.user.first_name} {self.user.last_name}"


class DepartmentOfficer(models.Model):

	CHOICES = (
		('Library','Library'),
		('Workshop','Workshop'),
		('MustSo','MustSo'),
		('Laboratories','Laboratories'),
		('Head Of Department','Head Of Department'),
		('Catering Office','Catering Office'),
		('Sports and Games','Sports and Games'),
		('Accomodation','Accomodation'),
		('Accounts Office','Accounts Office')
	)


	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
	department_name = models.CharField(max_length=100, choices=CHOICES)

	def __str__(self):
		return self.department_name

# class Department(models.Model):
# 	officer_name = models.CharField(max_length=100)
# 	department_name = models.CharField(max_length=100)
# 	clearance_item = models.CharField(max_length=200)
# 	student = models.ForeignKey(Student, on_delete=models.CASCADE)

# 	def __str__(self):
# 		return self.department_name


# @receiver(post_save, sender=User)
# def create_user(sender,instance,created,**kwargs):
# 	if created:
# 		Student.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user(sender,instance,created, **kwargs):
# 	instance.student.save()							
