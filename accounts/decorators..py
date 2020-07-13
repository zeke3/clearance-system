from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_pass_test


def student_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
	actual_decorator = user_pass_test(
		lambda u: u.is_active and u.is_student,
		login_url=login_url,
		redirect_field_name=redirect_field_name
		)

	if function:
		return actual_decorator(function)
	return actual_decorator
	

def teacher_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=login_url):
	actual_decorator = user_pass_test(
		lambda u: u.is_active and u.is_student,
		login_url=login_url,
		redirect_field_name=redirect_field_name
		)

	if function:
		return actual_decorator(function)
	return actual_decorator	
