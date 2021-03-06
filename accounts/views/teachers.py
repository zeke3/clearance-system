from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from ..forms import TeacherSignupForm, LoginForm
from ..models import User
from django.contrib import messages

#User = get_user_model()


class TeacherSignupView(CreateView):
	model =  User
	form_class = TeacherSignupForm
	template_name = 'accounts/signup.html'


	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'teacher'
		# print(self.request.resolver_match.route)
		return super().get_context_data(**kwargs)


	def form_valid(self, form):
		user = form.save()
		login(self.request, user)
		messages.success(self.request, f'Account created for {user.username}')
		return redirect('accounts:teacher-login')

		

# @login_required
# def home_view(request):
# 	return render(request,'accounts/home.html',{})


def login_view(request):
	# print(request.__dict__)
	# print(request.resolver_match.route)
	form = LoginForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():	
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('departments:upload')
			else:
				print("No user found")
	return render(request,'accounts/login.html',{"form":form})			

def logout_view(request):
	logout(request)
	return redirect('accounts:teacher-login')			