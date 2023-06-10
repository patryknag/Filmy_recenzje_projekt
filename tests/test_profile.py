import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
from filmy_app.models import Recenzent


@pytest.mark.django_db
def test_profile_view_returns_200():
    """
    Testuje, czy widok profilu zwraca poprawny kod odpowiedzi HTTP 200 po zalogowaniu użytkownika.
    """
    client = Client()
    user = User.objects.create_user(username='testuser', password='12345')
    recenzent = Recenzent.objects.create(user=user, name='Test Name', surname='Test Surname')
    client.login(username='testuser', password='12345')
    response = client.get(reverse('profile'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_profile_view_uses_correct_template():
    """
    Testuje, czy widok profilu używa poprawnego szablonu ('profile.html') po zalogowaniu użytkownika.
    """
    client = Client()
    user = User.objects.create_user(username='testuser', password='12345')
    recenzent = Recenzent.objects.create(user=user, name='Test Name', surname='Test Surname')
    client.login(username='testuser', password='12345')
    response = client.get(reverse('profile'))
    assert 'profile.html' in [template.name for template in response.templates]


@pytest.mark.django_db
def test_profile_view_returns_correct_recenzent():
    """
    Testuje, czy widok profilu zwraca poprawny profil recenzenta po zalogowaniu użytkownika.
    """
    client = Client()
    user = User.objects.create_user(username='testuser', password='12345')
    recenzent = Recenzent.objects.create(user=user, name='Test Name', surname='Test Surname')
