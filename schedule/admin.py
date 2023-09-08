from django.contrib import admin
from .models import Assignment


class AssignmentAdmin(admin.ModelAdmin):
    fields = ['user', 'course', 'title', 'description', 'date_created', 'due_date']

admin.site.register(Assignment, AssignmentAdmin)

