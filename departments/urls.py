from django.urls import path
from .views import *

app_name = 'departments'

urlpatterns = [
path('', UploadView, name='upload'),
path('1/<str:slug>/', LibraryFormView, name='add-form-library'),
path('2/<str:slug>/', WorkshopFormView, name='add-form-workshop'),
path('library/', library_search, name='library-search'),
path('workshop/', workshop_search, name='workshop-search'),
]