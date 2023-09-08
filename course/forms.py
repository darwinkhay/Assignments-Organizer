from django import forms
from .models import Document

class CourseForm(forms.Form):
    course_name = forms.CharField(max_length=200)

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['docfile']
