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


# @login_required
@teacher_required
def UploadView(request):
	template_name = 'departments/form.html'
	return render(request, template_name)


@library_officer_required
def LibraryFormView(request,slug):
	if request.method == 'POST':	
		form = LibraryForm(request.POST or None)
		if form.is_valid():
			form.save()
			return redirect('departments:add-form-library',slug)
	else:
		form = LibraryForm()

	context = { 'form': form }
	template_name = 'departments/upload.html'
	return render(request,template_name, context)


@workshop_officer_required
def WorkshopFormView(request,slug):
	user = request.user
	print(user)
	if request.method == 'POST':	
		form = WorkshopForm(request.POST or None)
		if form.is_valid():
			form.save()
			return redirect('departments:add-form-workshop',slug)
	else:
		form = WorkshopForm()
			
	context = { 'form': form }
	template_name = 'departments/upload.html'
	return render(request,template_name, context)
	

@library_officer_required
def library_search(request,slug, item):
	user = request.user.departmentofficer.department_name
	print(user)

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
	user = request.user.departmentofficer.department_name
	print(user)

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