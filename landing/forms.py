from django import forms
from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r'^\+?\d{9,15}$',
    message="Введите корректный номер телефона"
)

class ContactForm(forms.Form):
    full_name = forms.CharField(label="ФИО", max_length=100)
    phone = forms.CharField(label="Номер телефона", validators=[phone_validator], max_length=12)