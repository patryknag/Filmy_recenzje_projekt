import pytest
from django.urls import reverse
from django.test import Client


def test_home_view_returns_200():
    """
    Testuje, czy widok strony głównej zwraca poprawny kod odpowiedzi HTTP 200.
    """
    client = Client()
    response = client.get(reverse('home'))
    assert response.status_code == 200


def test_home_view_uses_correct_template():
    """
    Testuje, czy widok strony głównej używa poprawnego szablonu ('home.html').
    """
    client = Client()
    response = client.get(reverse('home'))
    assert 'home.html' in [template.name for template in response.templates]
