from django.db import models
from django.core.urlresolvers import reverse

class Contact(models.Model):

    salutation = models.CharField(choices=(
        (None, ''),
        ('Mr.', 'Mr.'),
        ('Ms.', 'Ms.'),
        ('Dr.', 'Dr.'),
        ('none', '')), max_length=5, 
        blank=True, default='none')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return ' '.join([self.first_name, self.last_name])

    def get_absolute_url(self):
        return reverse('contacts')

