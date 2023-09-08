from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .forms import CourseForm, DocumentForm
from .models import Course, Document

from schedule.models import Assignment
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch') # have to do this for classes
class CourseListView(generic.ListView):
    template_name = 'course/course_list.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        user_info = self.request.user
        cur_user = User.objects.get(username=user_info.username, email=user_info.email)
        return cur_user.course_set.all()

@method_decorator(login_required, name='dispatch') # have to do this for classes
class CourseDetailView(generic.DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c = get_object_or_404(Course, course_name=self.kwargs.get("course_name"))
        context['documents'] = c.document_set.all()
        context['assignments'] = Assignment.objects.filter(user_id=self.request.user.id).filter(course=c)
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Course, course_name=self.kwargs.get("course_name"))


@method_decorator(login_required, name='dispatch') # have to do this for classes
class CourseFormView(generic.FormView):
    template_name = 'course/course_form.html'
    form_class = CourseForm

    def get_context_data(self, **kwargs):
        user_info = self.request.user
        cur_user = User.objects.get(username=user_info.username, email=user_info.email)
        all_current_courses = Course.objects.all()
        context = super().get_context_data(**kwargs)
        context['course_list'] = all_current_courses
        return context

    def form_valid(self, form):
        user_info = self.request.user
        course_name = form.cleaned_data.get('course_name').upper()
        cur_user = User.objects.get(username=user_info.username, email=user_info.email)

        course, created = Course.objects.get_or_create(course_name=course_name)
        course.users.add(cur_user)
        return HttpResponseRedirect(reverse('course:list'))


@login_required
def DocumentFormView(request, course_name):
    message = 'Upload Notes!'
    course = Course.objects.get(course_name=course_name)
    if request.method == 'POST': # if the request is POST
        form = DocumentForm(request.POST, request.FILES) # creates a document
        if form.is_valid():
            doc = form.save(commit=False)
            doc.course = course
            doc.save()
            return HttpResponseRedirect(reverse('course:detail', kwargs={'course_name': course_name}))
        else:
            message = 'invalid form:'
    else:
        form = DocumentForm()  # A empty, unbound form, if they don't post

    # Render list page with the documents and the form
    context = {'course_name': course_name, 'form': form, 'message': message}
    return render(request, 'course/course_document_form.html', context)
