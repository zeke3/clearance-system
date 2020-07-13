from django.db import models
from accounts.models import Student

class MustSo(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	item = models.CharField(max_length=50)


class Library(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	item = models.CharField(max_length=50)


class Workshop(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	item = models.CharField(max_length=50)


class Laboratories(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	item = models.CharField(max_length=50)


class HeadOfDepartment(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	item = models.CharField(max_length=50)


class CateringOffice(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	item = models.CharField(max_length=50)


class SportsGames(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	item = models.CharField(max_length=50)


class Accomodation(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	item = models.CharField(max_length=50)


class AccountsOffice(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	item = models.CharField(max_length=50)
