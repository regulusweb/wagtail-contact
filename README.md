Provide a simple mixin which bakes a contact form(send emails on submit) into the inheriting classes, specifically Wagtail pages.

### Install
`pip install https://github.com/regulusweb/wagtail-contact/archive/master.zip`

Be sure to add `honeypot` and `wagtailcontact` to INSTALLED_APPS in settings.py.
The contact form uses `django-honeypot` to prevent automated form spam.


`django-honeypot` also requires a few settings to be declared in settings.py.
See [django-honeypot](https://github.com/jamesturk/django-honeypot) for more information.


### Usage
The Wagtail page you want to add this functionality should extend
`wagtailcontact.mixins.ContactMixin`.

When rendering the form in your page template be sure to add the honeypot field using the
`render_honeypot_field` tag. Otherwise a HTTP BadRequest will explode when you try to submit the form without this.

Like so:

`{% load honeypot %}`

And then within any form including the tag:

`{% render_honeypot_field %}`
