from django.core.validators import RegexValidator
from django import forms
from .models import Contact

phone_validator = RegexValidator(
    regex=r'^\d{11,12}$',
    message='Номер телефона должен содержать только 11 или 12 цифр'
)

class ContactForm(forms.ModelForm):
    phone_number = forms.CharField(
        validators=[phone_validator], 
        label="Номер телефона", 
        widget=forms.TextInput(attrs={'placeholder': 89995554433}))
    full_name = forms.CharField(
        label="ФИО",
        widget=forms.TextInput(attrs={'placeholder': "Иванов Иван Иванович"})
        )
    
    class Meta:
        model = Contact
        fields = ["full_name", "phone_number"]

    def clean(self):
        cleaned_data = super().clean()
        full_name = cleaned_data.get("full_name")

        if full_name and any(char.isdigit() for char in full_name):
            raise forms.ValidationError("Имя не должно содержать цифр")
        
        return cleaned_data