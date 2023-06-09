from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Gatunek(models.Model):
    """
    Model ten zawiera nazwy gatunków filmów.
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Film(models.Model):
    """
    Model z danymi dotyczącymi filmów
    """
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    director = models.CharField(max_length=200, null=True, blank=True)
    genres = models.ManyToManyField(Gatunek)

    def __str__(self):
        return self.title


class Recenzent(models.Model):
    """
    Model recenzenta - osoby wystawiającej opinię o filmie
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Opinia(models.Model):
    """
    Model umożliwiający wystawinie opinii filmu
    """
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    recenzent = models.ForeignKey(Recenzent, on_delete=models.CASCADE)
    text = models.TextField(null=True)

    def __str__(self):
        return f'Recenzja od: {self.recenzent.name} {self.recenzent.surname}'


class Ocena(models.Model):
    """
    Model z ocenami dla filmów
    """
    OCENA_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    ]
    opinia = models.OneToOneField(Opinia, on_delete=models.CASCADE)
    ocena = models.IntegerField(choices=OCENA_CHOICES)

    def __str__(self):
        return f'{self.opinia.recenzent.name} {self.opinia.recenzent.surname} ocena dla {self.opinia.film.title}'
