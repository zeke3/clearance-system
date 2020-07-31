from django.contrib import admin
from .models import *


# class LibraryAdmin(admin.ModelAdmin):
# 	readonly_fields = ('department_name',)

# admin.site.register(Library, LibraryAdmin)
admin.site.register(Library)
admin.site.register(Workshop)
admin.site.register(MustSo)
admin.site.register(Laboratories)
admin.site.register(HeadOfDepartment)
admin.site.register(CateringOffice)
admin.site.register(SportsGames)
admin.site.register(Accomodation)
admin.site.register(AccountsOffice)

# Register your models here.
