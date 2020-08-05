from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm, UserUpdateForm
from django.contrib import messages
from .decorators import student_required
from departments.models import *
from accounts.models import Student
from departments.models import *


cleared = ''

@login_required
@student_required
def HomeView(request):
	user = request.user
	student = Student.objects.get(user=user)
	library_items = len(Library.objects.all().filter(student_id=user.id))
	workshop_items = len(Workshop.objects.all().filter(student_id=user.id))
	mustso_items = len(MustSo.objects.all().filter(student_id=user.id))
	laboratories_items = len(Laboratories.objects.all().filter(student_id=user.id))
	hod_items = len(HeadOfDepartment.objects.all().filter(student_id=user.id))
	catering_office_items = len(CateringOffice.objects.all().filter(student_id=user.id))
	sports_games_items = len(SportsGames.objects.all().filter(student_id=user.id))
	accomodation_items = len(Accomodation.objects.all().filter(student_id=user.id))
	accounts_office_items = len(AccountsOffice.objects.all().filter(student_id=user.id))
	global cleared
	cleared = student.cleared
	if library_items == 0 and workshop_items == 0 and mustso_items == 0 and laboratories_items == 0 and hod_items == 0 and catering_office_items == 0 and sports_games_items == 0 and accomodation_items == 0 and accounts_office_items == 0:
		cleared = True
		student.save()	
	context = { 'cleared': cleared }
	template_name = 'students/home.html'
	return render(request, template_name, context)


# @login_required
@student_required
def ProfileUpdate(request):
	user = request.user
	student = Student.objects.get(user=user)
	if request.method == "POST":
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, instance=request.user.student)
		if u_form.is_valid() and p_form.is_valid():
			user = u_form.save()
			student = p_form.save(commit=False)
			student.user = user
			student.save()
			messages.success(request, f'Your account has been successfully updated')
			return redirect('students:student-home')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.student)
				
	context = { 
		'u_form' : u_form,
		'p_form' : p_form,
		'cleared' : cleared
	}
	template_name = 'students/profileupdate.html'
	return render(request, template_name, context)



####################### Items Views ################################
@student_required
def items_urls(request):
	user = request.user
	student = Student.objects.get(user=user)
	context = { 'cleared' : cleared }	
	template_name = 'students/items-urls.html'
	return render(request, template_name, context)	


@student_required	
def library_items(request):	
	items =[]
	user = request.user
	student = Student.objects.get(user=user)
	students = Library.objects.all().filter(student_id =user.id)
	# print(students)
	for student in students:
		items.append(student.item)
	context = { 'items': items, 'cleared': cleared }	
	template_name = 'students/items-list.html'
	return render(request, template_name, context)


@student_required	
def workshop_items(request):
	items =[]
	user = request.user
	student = Student.objects.get(user=user)
	# print(user.id)
	students = Workshop.objects.all().filter(student_id =user.id)
	# print(students)
	for student in students:
		items.append(student.item)
	context = { 'items': items, 'cleared': cleared }	
	template_name = 'students/items-list.html'
	return render(request, template_name, context)


@student_required	
def mustso_items(request):
	items =[]
	user = request.user
	student = Student.objects.get(user=user)
	# print(user.id)
	students = MustSo.objects.all().filter(student_id =user.id)
	# print(students)
	for student in students:
		items.append(student.item)
	context = { 'items': items, 'cleared': cleared }	
	template_name = 'students/items-list.html'
	return render(request, template_name, context)


@student_required	
def laboratories_items(request):
	items =[]
	user = request.user
	student = Student.objects.get(user=user)
	# print(user.id)
	students = Laboratories.objects.all().filter(student_id =user.id)
	# print(students)
	for student in students:
		items.append(student.item)
	context = { 'items': items, 'cleared': cleared }	
	template_name = 'students/items-list.html'
	return render(request, template_name, context)


@student_required	 
def hod_items(request):
	items =[]
	user = request.user
	student = Student.objects.get(user=user)
	# print(user.id)
	students = HeadOfDepartment.objects.all().filter(student_id =user.id)
	# print(students)
	for student in students:
		items.append(student.item)
	context = { 'items': items, 'cleared': cleared }	
	template_name = 'students/items-list.html'
	return render(request, template_name, context)


@student_required	
def catering_office_items(request):
	items =[]
	user = request.user
	student = Student.objects.get(user=user)
	# print(user.id)
	students = CateringOffice.objects.all().filter(student_id =user.id)
	# print(students)
	for student in students:
		items.append(student.item)
	context = { 'items': items, 'cleared': cleared }	
	template_name = 'students/items-list.html'
	return render(request, template_name, context)


@student_required	
def sports_games_items(request):
	items =[]
	user = request.user
	student = Student.objects.get(user=user)
	# print(user.id)
	students = SportsGames.objects.all().filter(student_id =user.id)
	# print(students)
	for student in students:
		items.append(student.item)
	context = { 'items': items, 'cleared': cleared }	
	template_name = 'students/items-list.html'
	return render(request, template_name, context)


@student_required	
def accomodation_items(request):
	items =[]
	user = request.user
	student = Student.objects.get(user=user)
	# print(user.id)
	students = Accomodation.objects.all().filter(student_id =user.id)
	# print(students)
	for student in students:
		items.append(student.item)
	context = { 'items': items, 'cleared': cleared }	
	template_name = 'students/items-list.html'
	return render(request, template_name, context)


@student_required	
def accounts_office_items(request):
	items =[]
	user = request.user
	student = Student.objects.get(user=user)
	# print(user.id)
	students = AccountsOffice.objects.all().filter(student_id =user.id)
	# print(students)
	for student in students:
		items.append(student.item)
	context = { 'items': items, 'cleared': cleared }	
	template_name = 'students/items-list.html'
	return render(request, template_name, context)
	

################### Request View #####################
@student_required
def request_dos(request):
	user = request.user
	student = Student.objects.get(user=user)
	if request.method == 'POST':
		student.request = True
		student.save()
		messages.success(request, f'Request has been sent to Dean Of Students')
		return redirect('students:student-home')
	context = { 'cleared' : cleared }	
	template_name = 'students/request-dos.html'
	return render(request, template_name, context)	