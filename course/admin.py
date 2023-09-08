from django.contrib import admin
from .models import Course, Document

class CourseAdmin(admin.ModelAdmin):
    fields = ['course_name', 'users']

class DocumentAdmin(admin.ModelAdmin):
    fields = ['course', 'docfile'] # course is the course the file is linked to

admin.site.register(Course, CourseAdmin)

admin.site.register(Document, DocumentAdmin)

