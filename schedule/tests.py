import datetime
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.utils import timezone
from .models import Assignment
from course.models import Course

class UserTest(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create(username="testing_user")
        user.set_password("password")
        user.save()

    def testLogin(self):
        # Tests whether a user object is created
        c = Client()
        logged_in = c.login(username="testing_user", password="password")
        self.assertTrue(logged_in)

def createAssignment(user, course, title, description,  due_date):

    return Assignment.objects.create(user=user, course=course, title=title, description=description, date_created=timezone.now(), due_date=due_date)

class AssignmentCreationTest(TestCase):
    def setUp(self):
        s = "do nothing"


    def testCreate(self):
        # Creates a new assignment and verifies it was saved in the database
        User = get_user_model()
        user = User.objects.create(username="testing_user")
        user.set_password("password")
        user.save()
        c = Client()
        c.login(username="testing_user", password="password")

        cours = Course.objects.create(course_name='cs3240')
        self.client.post('/course/form', data={'course_name': 'cs3240'})

        createAssignment(user = user, course = cours, title = "test_title",
                         description="test_desc", due_date = timezone.now()+datetime.timedelta(days=5))
        query = Assignment.objects.get(title="test_title")
        self.assertTrue(query)


        """
        response = c.post('/assignment/create/', {'course':'test_course', 'title':'test_title', 'desc':'test_desc',
                                                  'due_date':timezone.now()+datetime.timedelta(days=5)},  follow=True)
        self.assertEqual(response.status_code, 200)"""


    """
    def testCreateNotLoggedIn(self):
        # Verifies that an exception occurs if a user tries to submit an assignment without logging in (we should solve this by redirecting users to log in first)
        c = Client()
        """
