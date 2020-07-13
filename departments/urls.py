from django.urls import path
from .views import UploadView, FormView

app_name = 'departments'

urlpatterns = [
path('', UploadView, name='upload'),
path('form/', FormView, name='add-form'),
]