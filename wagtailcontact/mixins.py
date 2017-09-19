from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator

from honeypot.decorators import check_honeypot

from .forms import ContactForm


class ContactMixin():
    form_class = ContactForm
    success_url = None
    success_message = 'Thank you! We will get back to you as soon as possible.'

    def get_form(self, request):
        return self.form_class(request.POST or None)

    @method_decorator(check_honeypot)
    def serve(self, request, *args, **kwargs):
        self.form = self.get_form(request)
        if request.method == 'POST':
            if self.form.is_valid():
                self.form.save(page=self)  # Save triggers an email
                # Add a message to be displayed to the user
                messages.add_message(
                    request, messages.INFO,
                    self.get_success_message())
                # Redirect to the current page, to prevent resubmissions
                return HttpResponseRedirect(self.get_success_url())

        return super().serve(request, *args, **kwargs)

    def get_context(self, request):
        ctx = super().get_context(request)
        ctx['form'] = self.form
        return ctx

    def get_success_url(self):
        return self.success_url or self.url

    def get_success_message(self):
        return self.success_message
