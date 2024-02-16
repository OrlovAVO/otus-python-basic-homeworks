import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy



class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(
        help_text="Выберите дату не раньше сегодняшней, и не позже 28 дней."
    )

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        if data < datetime.date.today():
            raise ValidationError(gettext_lazy('Дата раньше сегодняшней!'))

        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(gettext_lazy('Дата позже 28 дней!'))
        return data
