import pytest
from django.urls import reverse
from django.test import Client
from filmy_app.models import Film, Recenzent, Opinia
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_wszystkie_opinie_view_returns_200(client):
    """
    Testuje, czy widok 'wszystkie_opinie' zwraca poprawny kod odpowiedzi HTTP 200.
    """
    response = client.get(reverse('wszystkie_opinie'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_wszystkie_opinie_view_uses_correct_template(client):
    """
    Testuje, czy widok 'wszystkie_opinie' używa poprawnego szablonu ('wszystkie_opinie.html').
    """
    response = client.get(reverse('wszystkie_opinie'))
    assert 'wszystkie_opinie.html' in [template.name for template in response.templates]
