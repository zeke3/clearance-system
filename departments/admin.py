from django.contrib import admin
from .models import *


# class LibraryAdmin(admin.ModelAdmin):
# 	readonly_fields = ('department_name',)

# admin.site.register(Library, LibraryAdmin)
admin.site.register(Library)
admin.site.register(Workshop)

# Register your models here.
