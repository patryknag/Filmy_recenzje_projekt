from filmy_app.forms import OpiniaForm, OcenaForm
from filmy_app.models import Film, Opinia, Ocena
from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_opinia_ocena_view_returns_forms_on_get(client, user):
    """
    Testuje, czy widok 'opinia_ocena' zwraca formularze opinii i oceny na żądanie GET.
    """
    film = Film.objects.create(title='Test Film')
    client.login(username='testuser', password='12345')
    response = client.get(reverse('opinia_ocena', kwargs={'film_id': film.id}))
    assert response.status_code == 200
    assert isinstance(response.context['form_opinia'], OpiniaForm)
    assert isinstance(response.context['form_ocena'], OcenaForm)


@pytest.mark.django_db
def test_opinia_ocena_view_creates_new_opinion_and_rating_on_post(client, user):
    """
    Testuje, czy widok 'opinia_ocena' tworzy nową opinię i ocenę na żądanie POST.
    """
    film = Film.objects.create(title='Test Film')
    client.login(username='testuser', password='12345')
    response = client.post(reverse('opinia_ocena', kwargs={'film_id': film.id}), {
        'text': 'Test Opinion',
        'ocena': 5,
    })
    assert response.status_code == 302
    assert Opinia.objects.count() == 1
    assert Ocena.objects.count() == 1


@pytest.mark.django_db
def test_opinia_ocena_view_redirects_after_successful_submission(client, user):
    """
    Testuje, czy widok 'opinia_ocena' przekierowuje po udanym przesłaniu formularzy.
    """
    film = Film.objects.create(title='Test Film')
    client.login(username='testuser', password='12345')
    response = client.post(reverse('opinia_ocena', kwargs={'film_id': film.id}), {
        'text': 'Test Opinion',
        'ocena': 5,
    }, follow=True)
    assert response.status_code == 200
    assert response.redirect_chain[-1] == (reverse('opinia_ocena', kwargs={'film_id': film.id}), 302)
