from django import forms
from contacts.models import Contact
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Layout, Fieldset, Div,
        ButtonHolder, Submit, HTML, MultiField, Field)



class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        exclude = [] 
    
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'add-contact'
        self.helper.add_input(Submit('submit', 'submit'))
        self.helper.method = "POST"
        self.helper.action = '/contacts/new'
        
        self.helper.layout = Layout(
                        Field('salutation', 
                            template='materialize/material.select.html'),
                        Field('first_name', template='materialize/text-basic.html'),
                        Field('last_name', template='materialize/text-basic.html'),
                        Field('email', template='materialize/email-basic.html',
                            id='id_email'),
                        Field('confirm_email', template='materialize/email-basic.html',
                            id='id_email'),
                )




