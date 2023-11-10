from django.contrib import admin
from .models import Grade


# Register your models here.
class GradeAdmin(admin.ModelAdmin):
    list_display = ('position', 'basic_salary')

admin.site.register(Grade, GradeAdmin)