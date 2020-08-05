from django.urls import path
from .views import *

app_name = 'students'

urlpatterns = [
	path('', HomeView, name='student-home'),
	path('update/', ProfileUpdate, name='student-update'),
	path('items/', items_urls, name='items-urls'),
	path('items/library/', library_items, name='library-items' ),
	path('items/workshop/', workshop_items, name='workshop-items' ),
	path('items/mustso/', mustso_items, name='mustso-items' ),
	path('items/laboratories/', laboratories_items, name='laboratories-items' ),
	path('items/head-of-department/', hod_items, name='hod-items' ),
	path('items/catering/', catering_office_items, name='catering-office-items' ),
	path('items/sports-games/', sports_games_items, name='sports-games-items' ),
	path('items/accomodation/', accomodation_items, name='accomodation-items' ),
	path('items/accounts-office/', accounts_office_items, name='accounts-office-items' ),
	path('request/dos', request_dos, name='request-dos')
]