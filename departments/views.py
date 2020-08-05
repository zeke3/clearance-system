from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# from accounts.decorators import teacher_required
from .decorators import *
from .forms import *
from accounts.models import Student, User
from django.db.models import Q
from .models import *
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.contrib import messages


# @login_required
@teacher_required
def UploadView(request):
	template_name = 'departments/form.html'
	return render(request, template_name)

################### Form Views ##########################
@library_officer_required
def LibraryFormView(request,slug):
	if request.method == 'POST':
		form = LibraryForm(request.POST or None)
		if form.is_valid():
			student = form.cleaned_data.get('student')
			if student.request:
				messages.info(request, f'This student is not permitted in lending an item')
			else:	
				form.save()
			return redirect('departments:add-form-library',slug)
	else:
		form = LibraryForm()

	context = { 'form': form }
	template_name = 'departments/upload.html'
	return render(request,template_name, context)


@workshop_officer_required
def WorkshopFormView(request,slug):
	if request.method == 'POST':
		form = WorkshopForm(request.POST or None)
		if form.is_valid():
			student = form.cleaned_data.get('student')
			if student.request:
				messages.info(request, f'This student is not permitted in lending an item')
			else:	
				form.save()
			return redirect('departments:add-form-workshop',slug)
	else:
		form = WorkshopForm()

	context = { 'form': form }
	template_name = 'departments/upload.html'
	return render(request,template_name, context)


@mustso_officer_required
def MustSoFormView(request,slug):
	if request.method == 'POST':
		form = MustSoForm(request.POST or None)
		if form.is_valid():
			student = form.cleaned_data.get('student')
			if student.request:
				messages.info(request, f'This student is not permitted in lending an item')
			else:	
				form.save()
			return redirect('departments:add-form-mustso',slug)
	else:
		form = MustSoForm()

	context = { 'form': form }
	template_name = 'departments/upload.html'
	return render(request,template_name, context)


@laboratories_officer_required
def LaboratoriesFormView(request,slug):
	if request.method == 'POST':
		form = LaboratoriesForm(request.POST or None)
		if form.is_valid():
			student = form.cleaned_data.get('student')
			if student.request:
				messages.info(request, f'This student is not permitted in lending an item')
			else:	
				form.save()
			return redirect('departments:add-form-laboratories',slug)
	else:
		form = LaboratoriesForm()

	context = { 'form': form }
	template_name = 'departments/upload.html'
	return render(request,template_name, context)


@hod_officer_required
def HeadOfDepartmentFormView(request,slug):
	if request.method == 'POST':
		form = HeadOfDepartmentForm(request.POST or None)
		if form.is_valid():
			student = form.cleaned_data.get('student')
			if student.request:
				messages.info(request, f'This student is not permitted in lending an item')
			else:	
				form.save()
			return redirect('departments:add-form-hod',slug)
	else:
		form = HeadOfDepartmentForm()

	context = { 'form': form }
	template_name = 'departments/upload.html'
	return render(request,template_name, context)


@catering_officer_required
def CateringOfficeFormView(request,slug):
	if request.method == 'POST':
		form = CateringOfficeForm(request.POST or None)
		if form.is_valid():
			student = form.cleaned_data.get('student')
			if student.request:
				messages.info(request, f'This student is not permitted in lending an item')
			else:	
				form.save()
			return redirect('departments:add-form-catering-office',slug)
	else:
		form = CateringOfficeForm()

	context = { 'form': form }
	template_name = 'departments/upload.html'
	return render(request,template_name, context)


@sports_games_officer_required
def SportsGamesFormView(request,slug):
	if request.method == 'POST':
		form = SportsGamesForm(request.POST or None)
		if form.is_valid():
			student = form.cleaned_data.get('student')
			if student.request:
				messages.info(request, f'This student is not permitted in lending an item')
			else:	
				form.save()
			return redirect('departments:add-form-sports-games',slug)
	else:
		form = SportsGamesForm()

	context = { 'form': form }
	template_name = 'departments/upload.html'
	return render(request,template_name, context)


@accomodation_officer_required
def AccomodationFormView(request,slug):
	if request.method == 'POST':
		form = AccomodationForm(request.POST or None)
		if form.is_valid():
			student = form.cleaned_data.get('student')
			if student.request:
				messages.info(request, f'This student is not permitted in lending an item')
			else:	
				form.save()
			return redirect('departments:add-form-accomodation',slug)
	else:
		form = AccomodationForm()

	context = { 'form': form }
	template_name = 'departments/upload.html'
	return render(request,template_name, context)


@accountsoffice_officer_required
def AccountsOfficeFormView(request,slug):
	if request.method == 'POST':
		form = AccountsOfficeForm(request.POST or None)
		if form.is_valid():
			student = form.cleaned_data.get('student')
			if student.request:
				messages.info(request, f'This student is not permitted in lending an item')
			else:	
				form.save()
			return redirect('departments:add-form-accounts-office',slug)
	else:
		form = AccountsOfficeForm()

	context = { 'form': form }
	template_name = 'departments/upload.html'
	return render(request,template_name, context)



################### Searching Views ######################
@library_officer_required
def library_search(request,slug, item):
	# user = request.user.departmentofficer.department_name
	# print(user)

	ctx = {}
	url_parameter = request.GET.get('q')
	if url_parameter:
		students = Library.objects.filter(Q(student__user__first_name__icontains=url_parameter) | Q(student__user__last_name__icontains=url_parameter))
	else:
		students = ''


	if slug == 'None' and item == 'None' :
		print('pass')
		pass
	else:
		if request.method == 'GET':
			print(slug)
			student = Library.objects.filter(Q(student_id=slug) and Q(item=item))
			student.delete()

	ctx['students'] = students

	if request.is_ajax():
		html = render_to_string(
			template_name='departments/library-results.html',
			context={'students':students}
		)

		data_dict = {"html_from_view": html}

		return JsonResponse(data=data_dict, safe=False)

	return render(request,'departments/search.html',ctx)


@workshop_officer_required
def workshop_search(request, slug, item):
	ctx = {}
	url_parameter = request.GET.get('q')
	if url_parameter:
		students = Workshop.objects.filter(Q(student__user__first_name__icontains=url_parameter) | Q(student__user__last_name__icontains=url_parameter))
	else:
		students = ''

	if slug is None and item is None:
		print('pass')
		pass
	else:
		if request.method == 'GET':
			print(slug)
			student = Workshop.objects.filter(Q(student_id=slug) and Q(item=item))
			student.delete()

	ctx['students'] = students

	if request.is_ajax():
		html = render_to_string(
			template_name='departments/workshop-results.html',
			context={'students':students}
		)

		data_dict = {"html_from_view": html}

		return JsonResponse(data=data_dict, safe=False)

	return render(request,'departments/search.html',ctx)


@mustso_officer_required
def mustso_search(request, slug, item):
	ctx = {}
	url_parameter = request.GET.get('q')
	if url_parameter:
		students = MustSo.objects.filter(Q(student__user__first_name__icontains=url_parameter) | Q(student__user__last_name__icontains=url_parameter))
	else:
		students = ''

	if slug is None and item is None:
		print('pass')
		pass
	else:
		if request.method == 'GET':
			print(slug)
			student = MustSo.objects.filter(Q(student_id=slug) and Q(item=item))
			student.delete()

	ctx['students'] = students

	if request.is_ajax():
		html = render_to_string(
			template_name='departments/mustso-results.html',
			context={'students':students}
		)

		data_dict = {"html_from_view": html}

		return JsonResponse(data=data_dict, safe=False)

	return render(request,'departments/search.html',ctx)


@laboratories_officer_required
def laboratories_search(request, slug, item):
	ctx = {}
	url_parameter = request.GET.get('q')
	if url_parameter:
		students = Laboratories.objects.filter(Q(student__user__first_name__icontains=url_parameter) | Q(student__user__last_name__icontains=url_parameter))
	else:
		students = ''

	if slug is None and item is None:
		print('pass')
		pass
	else:
		if request.method == 'GET':
			print(slug)
			student = Laboratories.objects.filter(Q(student_id=slug) and Q(item=item))
			student.delete()

	ctx['students'] = students

	if request.is_ajax():
		html = render_to_string(
			template_name='departments/laboratories-results.html',
			context={'students':students}
		)

		data_dict = {"html_from_view": html}

		return JsonResponse(data=data_dict, safe=False)

	return render(request,'departments/search.html',ctx)



@hod_officer_required
def hod_search(request, slug, item):
	ctx = {}
	url_parameter = request.GET.get('q')
	if url_parameter:
		students = HeadOfDepartment.objects.filter(Q(student__user__first_name__icontains=url_parameter) | Q(student__user__last_name__icontains=url_parameter))
	else:
		students = ''

	if slug is None and item is None:
		print('pass')
		pass
	else:
		if request.method == 'GET':
			print(slug)
			student = HeadOfDepartment.objects.filter(Q(student_id=slug) and Q(item=item))
			student.delete()

	ctx['students'] = students

	if request.is_ajax():
		html = render_to_string(
			template_name='departments/hod-results.html',
			context={'students':students}
		)

		data_dict = {"html_from_view": html}

		return JsonResponse(data=data_dict, safe=False)

	return render(request,'departments/search.html',ctx)



@catering_officer_required
def catering_office_search(request, slug, item):
	ctx = {}
	url_parameter = request.GET.get('q')
	if url_parameter:
		students = CateringOffice.objects.filter(Q(student__user__first_name__icontains=url_parameter) | Q(student__user__last_name__icontains=url_parameter))
	else:
		students = ''

	if slug is None and item is None:
		print('pass')
		pass
	else:
		if request.method == 'GET':
			print(slug)
			student = CateringOffice.objects.filter(Q(student_id=slug) and Q(item=item))
			student.delete()

	ctx['students'] = students

	if request.is_ajax():
		html = render_to_string(
			template_name='departments/catering-results.html',
			context={'students':students}
		)

		data_dict = {"html_from_view": html}

		return JsonResponse(data=data_dict, safe=False)

	return render(request,'departments/search.html',ctx)



@sports_games_officer_required
def sports_games_search(request, slug, item):
	ctx = {}
	url_parameter = request.GET.get('q')
	if url_parameter:
		students = SportsGames.objects.filter(Q(student__user__first_name__icontains=url_parameter) | Q(student__user__last_name__icontains=url_parameter))
	else:
		students = ''

	if slug is None and item is None:
		print('pass')
		pass
	else:
		if request.method == 'GET':
			print(slug)
			student = SportsGames.objects.filter(Q(student_id=slug) and Q(item=item))
			student.delete()

	ctx['students'] = students

	if request.is_ajax():
		html = render_to_string(
			template_name='departments/sports-games-results.html',
			context={'students':students}
		)

		data_dict = {"html_from_view": html}

		return JsonResponse(data=data_dict, safe=False)

	return render(request,'departments/search.html',ctx)



@accomodation_officer_required
def accomodation_search(request, slug, item):
	ctx = {}
	url_parameter = request.GET.get('q')
	if url_parameter:
		students = Accomodation.objects.filter(Q(student__user__first_name__icontains=url_parameter) | Q(student__user__last_name__icontains=url_parameter))
	else:
		students = ''

	if slug is None and item is None:
		print('pass')
		pass
	else:
		if request.method == 'GET':
			print(slug)
			student = Accomodation.objects.filter(Q(student_id=slug) and Q(item=item))
			student.delete()

	ctx['students'] = students

	if request.is_ajax():
		html = render_to_string(
			template_name='departments/accomodation-results.html',
			context={'students':students}
		)

		data_dict = {"html_from_view": html}

		return JsonResponse(data=data_dict, safe=False)

	return render(request,'departments/search.html',ctx)



@accountsoffice_officer_required
def accounts_office_search(request, slug, item):
	ctx = {}
	url_parameter = request.GET.get('q')
	if url_parameter:
		students = AccountsOffice.objects.filter(Q(student__user__first_name__icontains=url_parameter) | Q(student__user__last_name__icontains=url_parameter))
	else:
		students = ''

	if slug is None and item is None:
		print('pass')
		pass
	else:
		if request.method == 'GET':
			print(slug)
			student = AccountsOffice.objects.filter(Q(student_id=slug) and Q(item=item))
			student.delete()

	ctx['students'] = students

	if request.is_ajax():
		html = render_to_string(
			template_name='departments/accounts-office-results.html',
			context={'students':students}
		)

		data_dict = {"html_from_view": html}

		return JsonResponse(data=data_dict, safe=False)

	return render(request,'departments/search.html',ctx)



#################### DOS View ##########################

@dos_required
def dos_view(request):
	students = Student.objects.all().filter(request=True)
	
	if request.method == 'POST':
		for student in students:
			student_obj = DeanOfStudents()
			student_obj.student = student
			student_obj.approved = True
			student_obj.save()
		messages.success(request, "Students approved")
		return redirect('departments:upload')
	context = { 'students' : students}
	template_name = 'departments/dos.html'
	return render(request, template_name, context)


#################### Accounts Officer View ###################
@accounts_officer_required
def accounts_officer_view(request):
	students = DeanOfStudents.objects.order_by('student__user__first_name')
	context = { 'students' : students }
	template_name = 'departments/approved-students.html'
	return render(request,template_name,context)



#################### DOU VIew #############################
@dou_required
def dou_view(request):
	students = DeanOfStudents.objects.order_by('student__user__first_name')
	context = { 'students' : students }
	template_name = 'departments/approved-students.html'
	return render(request,template_name,context)	