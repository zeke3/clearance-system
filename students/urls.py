from django.urls import path
from .views import ProfileUpdate, HomeView

app_name = 'students'

urlpatterns = [
	path('', HomeView, name='student-home'),
	path('update/', ProfileUpdate, name='student-update'),
]