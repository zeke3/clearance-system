from django.db import models
from accounts.models import Student

class MustSo(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	item = models.CharField(max_length=50)
	lent_date = models.DateField(auto_now=True)

	def __str__(self):
		return f"{self.student}"


class Library(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	item = models.CharField(max_length=50)
	lent_date = models.DateField(auto_now=True)

	def __str__(self):
		return f"{self.student}"


class Workshop(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	item = models.CharField(max_length=50)
	lent_date = models.DateField(auto_now=True)

	def __str__(self):
		return f"{self.student}"


class Laboratories(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	item = models.CharField(max_length=50)
	lent_date = models.DateField(auto_now=True)

	def __str__(self):
		return f"{self.student}"


class HeadOfDepartment(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	item = models.CharField(max_length=50)
	lent_date = models.DateField(auto_now=True)

	def __str__(self):
		return f"{self.student}"


class CateringOffice(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	item = models.CharField(max_length=50)
	lent_date = models.DateField(auto_now=True)

	def __str__(self):
		return f"{self.student}"


class SportsGames(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	item = models.CharField(max_length=50)
	lent_date = models.DateField(auto_now=True)

	def __str__(self):
		return f"{self.student}"


class Accomodation(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	item = models.CharField(max_length=50)
	lent_date = models.DateField(auto_now=True)

	def __str__(self):
		return f"{self.student}"


class AccountsOffice(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	item = models.CharField(max_length=50)
	lent_date = models.DateField(auto_now=True)

	def __str__(self):
		return f"{self.student}"
