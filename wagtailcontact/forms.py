from django import forms
from django.conf import settings
from django.core.mail import EmailMessage
from django.template import loader


class ContactForm(forms.Form):

    subject_template = "contact/email/subject.txt"
    txt_template = "contact/email/message.txt"
    success_url = None

    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=200, required=True)
    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'cols': False}),
        required=True,
    )

    def get_email_context(self):
        ctx = self.cleaned_data
        ctx['subject_prefix'] = settings.EMAIL_SUBJECT_PREFIX
        return ctx

    def send_email(self, to, subject_template, txt_template, reply_to):
        context = self.get_email_context()
        from_email = settings.DEFAULT_FROM_EMAIL
        subject = loader.render_to_string(subject_template, context)
        message = loader.render_to_string(txt_template, context)
        msg = EmailMessage(
            subject.strip(),
            message,
            from_email,
            to,
            reply_to=reply_to
        )
        msg.send()

    def get_to(self, page):
        try:
            return [page.enquiry_email]
        except AttributeError:
             return [e for _, e in settings.MANAGERS]



    def save(self, page):
        # Forward enquiry
        to = self.get_to(page)
        reply_to = [self.cleaned_data['email']]
        self.send_email(to, self.subject_template, self.txt_template, reply_to)
