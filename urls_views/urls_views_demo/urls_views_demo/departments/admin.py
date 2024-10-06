from django.contrib import admin
from urls_views_demo.departments.models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass
