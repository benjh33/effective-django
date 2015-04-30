from django.conf.urls import patterns, url
from contacts.views import ContactView, CreateContactView

urlpatterns = patterns('',
        url(r'new$', CreateContactView.as_view(), name='create-contact'),
        url(r'$', ContactView.as_view(), name='contacts'),
        )

