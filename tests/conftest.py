import pytest
from django.conf import settings
from django.contrib.auth.models import User
from filmy_app.models import Recenzent, Film, Opinia
from django.test import Client


@pytest.fixture(autouse=True)
def configure_django_for_tests():
    if not settings.configured:
        settings.configure(INSTALLED_APPS=['filmy_app'])


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def recenzent(user):
    return Recenzent.objects.create(user=user, name='Test Name', surname='Test Surname')


@pytest.fixture
def film():
    return Film.objects.create(title='Test Film')


@pytest.fixture
def opinia1(recenzent, film):
    return Opinia.objects.create(film=film, recenzent=recenzent, text='Test Opinion 1')


@pytest.fixture
def opinia2(recenzent, film):
    return Opinia.objects.create(film=film, recenzent=recenzent, text='Test Opinion 2')


@pytest.fixture
def user(db):
    user = User.objects.create_user(username='testuser', password='12345')
    recenzent = Recenzent.objects.create(user=user, name='Test Name', surname='Test Surname')
    return user