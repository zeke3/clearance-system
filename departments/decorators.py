from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def teacher_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='accounts:teacher-login'):
	actual_decorator = user_passes_test(
		lambda u: u.is_active and u.is_teacher,
		login_url=login_url,
		redirect_field_name=redirect_field_name
		)

	if function:
		return actual_decorator(function)
	return actual_decorator	


def library_officer_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='accounts:teacher-login'):
	actual_decorator = user_passes_test(
		lambda u: u.departmentofficer.department_name == 'Library',
		login_url=login_url,
		redirect_field_name=redirect_field_name
		)

	if function:
		return actual_decorator(function)
	return actual_decorator	


def workshop_officer_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='accounts:teacher-login'):
	actual_decorator = user_passes_test(
		lambda u: u.departmentofficer.department_name == 'Workshop',
		login_url=login_url,
		redirect_field_name=redirect_field_name
		)

	if function:
		return actual_decorator(function)
	return actual_decorator		