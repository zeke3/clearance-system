from django.shortcuts import render
from .forms import UploadForm


def UploadView(request):
	template_name = 'departments/form.html'
	return render(request, template_name)


def FormView(request):
	form = UploadForm()
	context = { 'form': form }
	template_name = 'departments/upload.html'
	return render(request,template_name, context)
	