from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm, UserUpdateForm
from django.contrib import messages
from .decorators import student_required
from departments.models import *



@login_required
@student_required
def HomeView(request):
	# user = request.user
	# print(user)
	template_name = 'students/home.html'
	return render(request, template_name)


# @login_required
@student_required
def ProfileUpdate(request):
	if request.method == "POST":
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, instance=request.user.student)
		if u_form.is_valid() and p_form.is_valid():
			user = u_form.save()
			student = p_form.save(commit=False)
			student.user = user
			student.save()
			messages.success(request, f'Your account has been updated')
			return redirect('students:student-home')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.student)
				
	context = { 
		'u_form' : u_form,
		'p_form' : p_form
	}
	template_name = 'students/profileupdate.html'
	return render(request, template_name, context)


@student_required
def items_urls(request):
	template_name = 'students/items-urls.html'
	return render(request, template_name)	


@student_required	
def library_items(request):
	items =[]
	user = request.user
	# print(user.id)
	students = Library.objects.all().filter(student_id =user.id)
	# print(students)
	for student in students:
		items.append(student.item)
	context = { 'items': items }	
	template_name = 'students/items-list.html'
	return render(request, template_name, context)


@student_required	
def workshop_items(request):
	items =[]
	user = request.user
	# print(user.id)
	students = Workshop.objects.all().filter(student_id =user.id)
	# print(students)
	for student in students:
		items.append(student.item)
	context = { 'items': items }	
	template_name = 'students/items-list.html'
	return render(request, template_name, context)


@student_required	
def mustso_items(request):
	items =[]
	user = request.user
	# print(user.id)
	students = MustSo.objects.all().filter(student_id =user.id)
	# print(students)
	for student in students:
		items.append(student.item)
	context = { 'items': items }	
	template_name = 'students/items-list.html'
	return render(request, template_name, context)


@student_required	
def laboratories_items(request):
	items =[]
	user = request.user
	# print(user.id)
	students = Laboratories.objects.all().filter(student_id =user.id)
	# print(students)
	for student in students:
		items.append(student.item)
	context = { 'items': items }	
	template_name = 'students/items-list.html'
	return render(request, template_name, context)


@student_required	
def hod_items(request):
	items =[]
	user = request.user
	# print(user.id)
	students = HeadOfDepartment.objects.all().filter(student_id =user.id)
	# print(students)
	for student in students:
		items.append(student.item)
	context = { 'items': items }	
	template_name = 'students/items-list.html'
	return render(request, template_name, context)


@student_required	
def catering_office_items(request):
	items =[]
	user = request.user
	# print(user.id)
	students = CateringOffice.objects.all().filter(student_id =user.id)
	# print(students)
	for student in students:
		items.append(student.item)
	context = { 'items': items }	
	template_name = 'students/items-list.html'
	return render(request, template_name, context)


@student_required	
def sports_games_items(request):
	items =[]
	user = request.user
	# print(user.id)
	students = SportsGames.objects.all().filter(student_id =user.id)
	# print(students)
	for student in students:
		items.append(student.item)
	context = { 'items': items }	
	template_name = 'students/items-list.html'
	return render(request, template_name, context)


@student_required	
def accomodation_items(request):
	items =[]
	user = request.user
	# print(user.id)
	students = Accomodation.objects.all().filter(student_id =user.id)
	# print(students)
	for student in students:
		items.append(student.item)
	context = { 'items': items }	
	template_name = 'students/items-list.html'
	return render(request, template_name, context)


@student_required	
def accounts_office_items(request):
	items =[]
	user = request.user
	# print(user.id)
	students = AccountsOffice.objects.all().filter(student_id =user.id)
	# print(students)
	for student in students:
		items.append(student.item)
	context = { 'items': items }	
	template_name = 'students/items-list.html'
	return render(request, template_name, context)
	