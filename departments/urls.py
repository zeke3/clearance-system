from django.urls import path
from .views import *

app_name = 'departments'

urlpatterns = [
path('', UploadView, name='upload'),
path('1/<str:slug>/', LibraryFormView, name='add-form-library'),
path('2/<str:slug>/', WorkshopFormView, name='add-form-workshop'),
path('3/<str:slug>/', MustSoFormView, name='add-form-mustso'),
path('4/<str:slug>/', LaboratoriesFormView, name='add-form-laboratories'),
path('5/<str:slug>/', HeadOfDepartmentFormView, name='add-form-hod'),
path('6/<str:slug>/', CateringOfficeFormView, name='add-form-catering-office'),
path('7/<str:slug>/', SportsGamesFormView, name='add-form-sports-games'),
path('8/<str:slug>/', AccomodationFormView, name='add-form-accomodation'),
path('9/<str:slug>/', AccountsOfficeFormView, name='add-form-accounts-office'),
path('library/<str:slug>/<str:item>/', library_search, name='library-search'),
path('workshop/<str:slug>/<str:item>/', workshop_search, name='workshop-search'),
path('mustso/<str:slug>/<str:item>/', mustso_search, name='mustso-search'),
path('laboratories/<str:slug>/<str:item>/', laboratories_search, name='laboratories-search'),
path('head-of-department/<str:slug>/<str:item>/', hod_search, name='hod-search'),
path('catering-office/<str:slug>/<str:item>/', catering_office_search, name='catering-office-search'),
path('sports-games/<str:slug>/<str:item>/', sports_games_search, name='sports-games-search'),
path('accomodation/<str:slug>/<str:item>/', accomodation_search, name='accomodation-search'),
path('accounts-office/<str:slug>/<str:item>/', accounts_office_search, name='accounts-office-search'),
]