from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from .models import Course, Document
from .forms import DocumentForm
from django.core.files.uploadedfile import SimpleUploadedFile
import os
from schedule.static import *


class CourseTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', email='test@testing.com', password='password')
        self.client = Client()
        self.client.login(username='test', password='password')

    def test_create_course(self):
        self.client.post('/course/form/', data={'course_name':'sts1500'})
        self.client.post('/course/form/', data={'course_name':'cs3240'})
        self.client.post('/course/form/', data={'course_name':'dracula'})

        course_list = self.user.course_set.values_list('course_name', flat=True)
        self.assertSequenceEqual(course_list, ['STS1500', 'CS3240', 'DRACULA'])
    """
    def test_course_list(self):
        self.client.post('/course/form/', data={'course_name':'sts1500'})
        self.client.post('/course/form/', data={'course_name':'cs3240'})
        self.client.post('/course/form/', data={'course_name':'dracula'})

        response = self.client.get('/course/')
        self.assertContains(response, 'STS1500')
        self.assertContains(response, 'CS3240')
        self.assertContains(response, 'DRACULA')

    def test_user_list_in_course(self):
        self.client.post('/course/form/', data={'course_name':'sts1500'})
        get_user_model().objects.create_user(username='other', email='other@testing.com', password='password')
        self.client.login(username='other', password='password')
        self.client.post('/course/form/', data={'course_name':'sts1500'})

        response = self.client.get('/course/STS1500/')
        self.assertContains(response, 'test')
        self.assertContains(response, 'other')
    """
    def test_signup_course(self):
        Course.objects.create(course_name='cs3240')
        old_len = len(Course.objects.all())
        self.client.post('/course/form', data={'course_name':'cs3240'})
        new_len = len(Course.objects.all())
        self.assertEqual(old_len, new_len)

class FileUploadTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', email='test@testing.com',password='chonkycookies123')
        self.client = Client()
        self.client.login(username='test',password='chonkycookies123')
    
    def test_upload_file(self):
        
        # Add in a course first
        self.client.post('/course/form/', data={'course_name':'cs3240'})
        course_added = Course.objects.get(course_name='CS3240')
        
        # Upload a pdf for the course
        
        pdf = SimpleUploadedFile('randomnotes.pdf',b'random content in pdf', content_type='application/pdf')
        document = Document(course=course_added, docfile=pdf)
      
        document.save()

        # check to see if document has been uploaded
        self.assertEqual(str(document.filename()), pdf.name)

        # check to see if document is under correct course
        self.assertEqual(document.course, course_added)
        #os.remove(document.docfile.path) # remove file

    def test_file_list(self):
        # Add in a course first
        self.client.post('/course/form/', data={'course_name':'cs3710'})
        course_added1 = Course.objects.get(course_name='CS3710')


        # Upload a pdf for the course
        
        pdf1 = SimpleUploadedFile('randomnotes1.pdf',b'random content in pdf', content_type='application/pdf')
        document1 = Document(course=course_added1, docfile=pdf1)
      
        document1.save()

        # Upload another pdf for the course
        
        pdf2 = SimpleUploadedFile('randomnotes2.pdf',b'random content in pdf', content_type='application/pdf')
        document2 = Document(course=course_added1, docfile=pdf2)
      
        document2.save()


        # Upload a pdf for the course
        
        pdf3 = SimpleUploadedFile('randomnotes3.pdf',b'random content in pdf', content_type='application/pdf')
        document3 = Document(course=course_added1, docfile=pdf3)
      
        document3.save()

        doclist = course_added1.document_set.values_list('docfile',flat=True)

        self.assertSequenceEqual(doclist, [document1.docfile,document2.docfile,document3.docfile]) # check to see if course has the documents in its list
    
        # remove temporary test files
        #os.remove(document1.docfile.path)
        #os.remove(document2.docfile.path)
        #os.remove(document3.docfile.path)
