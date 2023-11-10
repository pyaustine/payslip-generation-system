from django.contrib import admin
from .models import Grade, Staff


# Register your models here.
class GradeAdmin(admin.ModelAdmin):
    list_display = ('position', 'basic_salary')

class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gross_salary')

admin.site.register(Grade, GradeAdmin)
admin.site.register(Staff, StaffAdmin)