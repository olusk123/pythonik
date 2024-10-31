from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class Osoba(models.Model):
    nazwa = models.CharField(max_length=100)
    data_dodania = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.nazwa.isalpha():
            raise ValidationError('Nazwa może zawierać tylko litery.')

        if self.data_dodania is not None and self.data_dodania > timezone.now():
            raise ValidationError('Data dodania nie może być z przyszłości.')

class Team(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Person(models.Model):
    SHIRT_SIZES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]

    MONTHS = [
        (1, 'Styczeń'),
        (2, 'Luty'),
        (3, 'Marzec'),
        (4, 'Kwiecień'),
        (5, 'Maj'),
        (6, 'Czerwiec'),
        (7, 'Lipiec'),
        (8, 'Sierpień'),
        (9, 'Wrzesień'),
        (10, 'Październik'),
        (11, 'Listopad'),
        (12, 'Grudzień'),
    ]

    name = models.CharField(max_length=100)
    shirt_size = models.CharField(max_length=2, choices=SHIRT_SIZES, default='S')
    miesiac_dodania = models.IntegerField(choices=MONTHS, default=1)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nazwa