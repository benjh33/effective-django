from unittest import TestCase
from contacts.models import Contact

class ContactTests(TestCase):
    
    def test_string_method(self):
        contact = Contact(first_name='Ben',
                last_name='Hunter')
        self.assertEquals(str(contact),
                'Ben Hunter')


