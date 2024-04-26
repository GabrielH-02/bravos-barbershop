from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import HairRequestForm

# Create your tests here.
class TestAboutView(TestCase):


    def setUp(self):
        """Creates about me content"""
        self.about_content = About(content="This is about me.")
        self.about_content.save()
        

    def test_render_about_page_with_hair_request_form(self):
        """Verifies get request for about me containing a hair request form"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(
            response.context['hairrequest_form'], HairRequestForm)


    def test_successful_collaboration_request_submission(self):
        """Test for a user requesting a hair request"""
        post_data = {
            'name': 'test name',
            'email': 'test@gmail.com',
            'phone_number': '0909903394992',
            'subject': 'test subject',
            'message': 'test message'
        }
        response = self.client.post(reverse('about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"You're Hair request has been received! We will contact you shortly ...", response.content)
