from django.urls import path
from .views import CourseListView, CourseFormView, CourseDetailView, DocumentFormView
from . import views
app_name = 'course'
urlpatterns = [
    path('', CourseListView.as_view(), name='list'),
    path('form/', CourseFormView.as_view(), name='form'),
    # path('notes/', views.UploadDocumentFormView, name='upload'),
    path('<str:course_name>/', CourseDetailView.as_view(), name='detail'),
    path('<str:course_name>/notes/', views.DocumentFormView, name='upload'), # goes to the file list for class
]
