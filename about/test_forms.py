from django.test import TestCase
from .forms import HairRequestForm


class TestHairRequestForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = HairRequestForm({
            'name': 'test',
            'email': 'test@test.com',
            'phone_number': '010223679785',
            'subject': 'I need help with my hair', 
            'message': 'Help me please, its blue!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")
    
    def test_name_is_required(self):
        """Test for the 'name' field"""
        form = HairRequestForm({
            'name': '',
            'email': 'test@test.com',
            'phone_number': '010223679785',
            'subject': 'I need help with my hair', 
            'message': 'Help me please, its blue!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Name was not provided, but the form is valid"
        )

    def test_email_is_required(self):
        """Test for the 'email' field"""
        form = HairRequestForm({
            'name': 'test',
            'email': '',
            'phone_number': '010223679785',
            'subject': 'I need help with my hair', 
            'message': 'Help me please, its blue!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Email was not provided, but the form is valid"
        )
    
    def test_phone_number_is_required(self):
        """Test for the 'phone_number' field"""
        form = HairRequestForm({
            'name': 'test',
            'email': 'test@test.com',
            'phone_number': '',
            'subject': 'I need help with my hair', 
            'message': 'Help me please, its blue!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Phone Number was not provided, but the form is valid"
        )

    def test_subject_is_required(self):
        """Test for the 'subject' field"""
        form = HairRequestForm({
            'name': 'test',
            'email': 'test@test.com',
            'phone_number': '010223679785',
            'subject': '', 
            'message': 'Help me please, its blue!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Subject was not provided, but the form is valid"
        )

    def test_message_is_required(self):
        """Test for the 'message' field"""
        form = HairRequestForm({
            'name': 'test',
            'email': 'test@test.com',
            'phone_number': '010223679785',
            'subject': 'I need help with my hair', 
            'message': ''
        })
        self.assertFalse(
            form.is_valid(),
            msg="Message was not provided, but the form is valid"
        )
