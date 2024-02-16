import datetime
from django.test import TestCase
from catalog.forms import RenewBookForm


class RenewBookFormTest(TestCase):

    def test_renew_form_date_in_past(self):
        print('Начало test_renew_form_date_in_past')
        date = datetime.date.today() - datetime.timedelta(days=1)
        form = RenewBookForm(data={'renewal_date': date})
        self.assertFalse(form.is_valid())
        print('Конец test_renew_form_date_in_past')

    def test_renew_form_date_too_far_in_future(self):
        print('Начало test_renew_form_date_too_far_in_future')
        date = datetime.date.today() + datetime.timedelta(weeks=4) + datetime.timedelta(days=1)
        form = RenewBookForm(data={'renewal_date': date})
        self.assertFalse(form.is_valid())
        print('Конец test_renew_form_date_too_far_in_future')

    def test_renew_form_date_today(self):
        print('Начало test_renew_form_date_today')
        date = datetime.date.today()
        form = RenewBookForm(data={'renewal_date': date})
        self.assertTrue(form.is_valid())
        print('Конец test_renew_form_date_today')

    def test_renew_form_date_max(self):
        print('Начало test_renew_form_date_max')
        date = datetime.date.today() + datetime.timedelta(weeks=4)
        form = RenewBookForm(data={'renewal_date': date})
        self.assertTrue(form.is_valid())
        print('Конец test_renew_form_date_max')

    def test_renew_form_date_field_label(self):
        print('Начало test_renew_form_date_field_label')
        form = RenewBookForm()
        self.assertTrue(
            form.fields['renewal_date'].label is None or
            form.fields['renewal_date'].label == 'renewal date')
        print('Конец test_renew_form_date_field_label')

    def test_renew_form_date_field_help_text(self):
        print('Начало test_renew_form_date_field_help_text')
        form = RenewBookForm()
        self.assertEqual(
            form.fields['renewal_date'].help_text,
            'Выберите дату не раньше сегодняшней, и не позже 28 дней.')
        print('Конец test_renew_form_date_field_help_text')
