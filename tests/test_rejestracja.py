from django.test import Client
from django.urls import reverse
from filmy_app.models import Recenzent
from django.contrib.auth.models import User
import pytest
from filmy_app.forms import RejestracjaRecenzentaForm


@pytest.mark.django_db
def test_rejestracja_recenzenta_view_returns_registration_form_on_get(client):
    """
    Testuje, czy widok 'rejestracja_recenzenta' zwraca formularz rejestracji na żądanie GET.
    """
    response = client.get(reverse('rejestracja'))
    assert response.status_code == 200
    assert isinstance(response.context['form'], RejestracjaRecenzentaForm)


@pytest.mark.django_db
def test_rejestracja_recenzenta_view_creates_new_recenzent_on_post(client):
    """
    Testuje, czy widok 'rejestracja_recenzenta' tworzy nowego recenzenta na żądanie POST.
    """
    form_data = {
        'username': 'testuser',
        'password': 'testpassword',
        'password_confirm': 'testpassword',
        'name': 'Test',
        'surname': 'User',
    }
    response = client.post(reverse('rejestracja'), data=form_data)
    assert User.objects.filter(username='testuser').exists()
    assert Recenzent.objects.filter(name='Test', surname='User').exists()


@pytest.mark.django_db
def test_rejestracja_recenzenta_view_redirects_after_successful_registration(client):
    """
    Testuje, czy widok 'rejestracja_recenzenta' przekierowuje po pomyślnej rejestracji.
    """
    form_data = {
        'username': 'testuser',
        'password': 'testpassword',
        'password_confirm': 'testpassword',
        'name': 'Test',
        'surname': 'User',
    }
    response = client.post(reverse('rejestracja'), data=form_data)
    assert response.status_code == 302
    assert response.url == reverse('home')
