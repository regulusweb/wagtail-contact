from django.test import TestCase

from wagtailcontact.templatetags.wagtailcontact_tags import bleachclean


class WagtailContactTagsTestCase(TestCase):

    def test_bleanclean_cleandata(self):
        cleaned = bleachclean('Hello')
        self.assertEqual(cleaned, 'Hello')

    def test_bleanclean_strips(self):
        cleaned = bleachclean('<script>evil</script>')
        self.assertEqual(cleaned, 'evil')
