from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="ФИО")
    phone_number = models.CharField(max_length=12, verbose_name="Номер телефона")

    def __str__(self) -> str:
        return self.full_name