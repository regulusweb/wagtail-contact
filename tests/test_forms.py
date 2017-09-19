from django.core import mail
from django.test import TestCase

from wagtailcontact.forms import ContactForm


class ContactFormTestCase(TestCase):

    valid_data = {'name': 'test', 'email': 't@t.com', 'message': 'Hi'}

    def test_required_fields(self):
        form = ContactForm()
        self.assertTrue(
            all([
                form.fields['email'].required,
                form.fields['name'].required,
                form.fields['message'].required
            ])
        )

    def test_form_valid(self):
        form = ContactForm(data=self.valid_data.copy())
        self.assertTrue(form.is_valid())

    def test_send_email(self):
        data = self.valid_data.copy()
        data['message'] = 'Hello good people'
        form = ContactForm(data=data)
        form.is_valid()  # trigger to populate cleaned_data
        reply_to = [form.cleaned_data['email']]
        form.send_email(['to@g.com'], form.subject_template, form.txt_template, reply_to)

        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('Hello good people', mail.outbox[0].body)
