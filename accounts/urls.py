from django.urls import path
from accounts.views import students, teachers


app_name = 'accounts'

urlpatterns = [
	# path('home/', teachers.home_view, name='home'),
	path('login/student/', students.login_view, name='student-login'),
	path('login/teacher/', teachers.login_view, name='teacher-login'),
	path('logout/teacher/', teachers.logout_view, name='logout-teacher'),
	path('logout/student/', students.logout_view, name='logout-student'),
	#path('home_students', students.home_view, name='home'),
	path('signup/teachers/', teachers.TeacherSignupView.as_view(), name='teacher_signup'),
	path('signup/students/', students.StudentSignupView, name='student_signup'),
]

