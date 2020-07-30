from django.urls import path
from .views import *

app_name = 'students'

urlpatterns = [
	path('', HomeView, name='student-home'),
	path('update/', ProfileUpdate, name='student-update'),
	path('items/', items_urls, name='items-urls'),
	path('items/library/', library_items, name='library-items' ),
	path('items/workshop/', workshop_items, name='workshop-items' ),
]