"""
/*

*  REFERENCES
*  Title: <HOW TO CREATE A CALENDAR USING DJANGO>
*  Author: <Hui Wen>
*  Date: <11/17/2021>
*  Code version: <N/A>
*  URL: <https://www.huiwenteo.com/normal/2018/07/24/django-calendar.html>
*  Software License: <N/A>
*

*/

"""


from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .models import Assignment
from course.models import Course
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from datetime import datetime, timedelta, date
from django.utils.safestring import mark_safe
from .utils import Calendar
import calendar


# from here to the #----------- line referenced Hui Wen's calendar creation tutorial
# calendar creation view
@login_required # requires login before viewing
def CalendarView(request, year, month):

    # filter assignments by users
    assignments = Assignment.objects.filter(user_id=request.user.id)
    # use today's date for the calendar
    #d = get_date(request.GET.get('day', None))
    # Instantiate our calendar class with today's year and date
    cal = Calendar(year, month)
    # Call the formatmonth method, which returns our calendar as a table
    html_cal = cal.formatmonth(assignments, withyear=True) # pass list of assignments in

    #get month
    d = get_date(year, month)
    # prev_month =

    return render(request, 'schedule/calendar.html',
                  {'calendar': mark_safe(html_cal), 'prev_month': prev_month(d), 'next_month': next_month(d)})


# this is just for when user clicks on calendar button on navbar
@login_required # requires login before viewing
def CalendarRedirect(request):
    d = datetime.today()
    return redirect(str(d.year) + '/' + str(d.month)+ '/')

# gets the date based on year and month and formats it
def get_date(year, month):
    if year and month:
        return date(year, month, day=1)
    return datetime.today()

# gets the previous month,
def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = (prev_month.year, prev_month.month)
    return month

# returns next month and the year it comes with
def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = (next_month.year, next_month.month)
    return month

#------------------------------------------------------------------------------------------------------


@login_required # requires login before viewing
def index(request):
    return render(request, 'schedule/index.html')

@method_decorator(login_required, name='dispatch') # have to do this for classes
class IndexView(generic.ListView):
    template_name = 'schedule/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Assignment.objects.filter(user_id=self.request.user.id).order_by('-due_date').reverse()[:5]

@login_required # requires login before viewing
def assignment_form(request): # make sure it's linked with users
    return render(request, 'schedule/assignment_form.html',
    {'course_list': Course.objects.filter(users=request.user).values().order_by('course_name')})
    # filters by users and orders by course name


@method_decorator(login_required, name='dispatch') # have to do this for classes
class AssignmentListView(generic.ListView):
    template_name = 'schedule/assignment_list.html'
    context_object_name = 'assignment_list'
    def get_queryset(self):
        order = self.request.GET.get('sort', 'due_date')
        if(order == 'course'):
            return Assignment.objects.filter(user_id=self.request.user.id).order_by('course__course_name')
        return list(Assignment.objects.filter(user_id=self.request.user.id).order_by(order))

@login_required # requires login before viewing
def create_assignment(request):
    if (request.method == 'POST'):
        course = Course.objects.get(course_name=request.POST["course"])
        title = request.POST["title"]
        desc = request.POST["desc"]
        due_date = request.POST["due_date"]
        if (not course or not title or not desc or not due_date):
            return render(request, 'schedule/assignment_form.html', {
                'error_message': "Please fill out the text boxes.",
                'course_list': Course.objects.filter(users=request.user).values().order_by('course_name')
            })
        if (len(title) > 200):
            return render(request, 'schedule/assignment_form.html', {
                'error_message2': "Assignment title too long",
            })
        Assignment.objects.create( # when assignment is created,
            user_id = request.user.id, # user id associated with this assignment is set to current user
            course = course,
            title = title,
            description = desc,
            date_created = timezone.now(),
            due_date = due_date
        )
    return HttpResponseRedirect(reverse('schedule:assignment_list'))

@login_required # requires login before viewing
def delete_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    assignment.delete()
    return HttpResponseRedirect(reverse('schedule:assignment_list'))

