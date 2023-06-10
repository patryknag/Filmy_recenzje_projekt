import pytest
from django.urls import reverse
from django.test import Client
from filmy_app.models import Gatunek, Film


@pytest.mark.django_db
def test_gatunki_filmy_view_returns_200():
    """
    Testuje, czy widok 'gatunki_filmy' zwraca poprawny kod odpowiedzi HTTP 200.
    """
    client = Client()
    response = client.get(reverse('gatunki_filmy'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_gatunki_filmy_view_uses_correct_template():
    """
    Testuje, czy widok 'gatunki_filmy' używa poprawnego szablonu ('gatunki_filmy.html').
    """
    client = Client()
    response = client.get(reverse('gatunki_filmy'))
    assert 'gatunki_filmy.html' in [template.name for template in response.templates]


@pytest.mark.django_db
def test_gatunki_filmy_view_returns_all_gatunki_and_filmy():
    """
    Testuje, czy widok 'gatunki_filmy' zwraca wszystkie obiekty Gatunek i Film.
    """
    client = Client()

    # Tworzenie przykładowych danych
    gatunek1 = Gatunek.objects.create(name='Test Gatunek 1')
    gatunek2 = Gatunek.objects.create(name='Test Gatunek 2')
    film1 = Film.objects.create(title='Test Film 1')
    film2 = Film.objects.create(title='Test Film 2')

    response = client.get(reverse('gatunki_filmy'))

    # Sprawdzanie, czy odpowiedź zawiera wszystkie obiekty Gatunek i Film
    assert len(response.context['gatunki']) == Gatunek.objects.count()
    assert len(response.context['filmy']) == Film.objects.count()
    assert gatunek1 in response.context['gatunki']
    assert gatunek2 in response.context['gatunki']
    assert film1 in response.context['filmy']
    assert film2 in response.context['filmy']
