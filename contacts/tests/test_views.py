from django.test.client import Client, RequestFactory
from django.test import TestCase
from contacts.models import Contact

class ContactListViewTest(TestCase):
    
    def setUp(self):
        self.client = Client()

    def test_contact_in_context(self):
        response = self.client.get('/contacts/')

        self.assertEquals(list(response.context['object_list']), [])
        contact = Contact.objects.create(first_name='foo', last_name='bar', 
                email="baz@bar.com")
        response = self.client.get('/contacts/')
        self.assertEqual(list(response.context['object_list'])[0], contact) 

    def test_form_renders_on_list_page(self):
        response = self.client.get('/contacts/')
        self.assertTemplateUsed(response, 'base.html')

    def test_data_from_submitted_from_shows_on_contact_list(self):
        return True


class ContactCreateViewTest(TestCase):

    def test_create_form_does_not_save_incomplete_form(self):
        return True

    def test_create_form_saves_complete_form(self):
        return True
