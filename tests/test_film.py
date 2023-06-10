import pytest
from django.urls import reverse
from filmy_app.models import Film
from django.test import Client
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'Filmy_projekt.settings'


@pytest.mark.django_db
def test_film_view_returns_200(client):
    """
    Testuje, czy widok zwraca poprawny kod odpowiedzi HTTP 200.
    Tworzy przykładowy obiekt filmu, a następnie sprawdza, czy odpowiedź na żądanie GET do widoku filmu ma status 200.
    """
    client = Client()
    film = Film.objects.create(title='Test Film')
    response = client.get(reverse('film', args=[film.pk]))
    assert response.status_code == 200


@pytest.mark.django_db
def test_film_view_displays_correct_title(client):
    """
    Testuje, czy widok poprawnie wyświetla tytuł filmu na stronie.
    Tworzy przykładowy obiekt filmu, a następnie sprawdza, czy tytuł filmu jest zawarty w treści odpowiedzi na żądanie GET do widoku filmu.
    """
    client = Client()
    film = Film.objects.create(title='Test Film')
    response = client.get(reverse('film', args=[film.pk]))
    assert 'Test Film' in str(response.content)
