from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from ..forms import StudentSignupForm,LoginForm, StudentProfileForm
from ..models import User, Student
from django.contrib import messages

#User = get_user_model()


# class StudentSignupView(CreateView):
# 	model = User
# 	form_class = StudentSignupForm
# 	template_name = 'accounts/signup.html'
	
# 	def get_context_data(self,**kwargs):
# 		kwargs['user_type'] = 'student'
# 		return super().get_context_data(**kwargs)

# 	def form_valid(self,form):
# 		user = form.save()
# 		login(self.request, user)
# 		return redirect('accounts:home')	


def StudentSignupView(request, *args):
	if request.method == 'POST':
		signup_form = StudentSignupForm(request.POST or None)
		profile_form = StudentProfileForm(request.POST or None)
		if signup_form.is_valid() and profile_form.is_valid():
			user = signup_form.save()
			student = profile_form.save(commit=False)
			student.user = user
			student.save()
			return redirect('students:student-home')
	else:
		signup_form = StudentSignupForm()
		profile_form = StudentProfileForm()

	template_name = 'accounts/signup.html'
	context = {'signup_form' : signup_form, 'profile_form': profile_form }
	return render(request, template_name, context)

			

@login_required
def home_view(request):
	return render(request,'students/home.html')


def login_view(request):
	form = LoginForm(request.POST or None)
	if request.method == 'POST': 
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('students:student-home')
			else:
				print("User not found")	
	return render(request, 'accounts/login.html',{ 'form': form})		

def logout_view(request):
	logout(request)
	return redirect('acconts:student-login')	