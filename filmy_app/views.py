from django.shortcuts import render, redirect, get_object_or_404
from .models import Film, Gatunek, Opinia, Recenzent
from django.contrib.auth.decorators import login_required
from .forms import OpiniaForm, OcenaForm, RejestracjaRecenzentaForm


# Create your views here.
def home(request):
    """
    Strona główna
    """
    return render(request, 'home.html')


def gatunki_filmy(request):
    """
    Wyświetla wszystkie gatunki i filmy
    """
    gatunki = Gatunek.objects.all()
    filmy = Film.objects.all()
    return render(request, 'gatunki_filmy.html', {'gatunki': gatunki, 'filmy': filmy})


def film(request, pk):
    """
    Wyświetla szczegółowe informacje o filmie.
    """
    film = get_object_or_404(Film, pk=pk)
    return render(request, 'film.html', {'film': film})


@login_required
def opinia_ocena(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    opinie = Opinia.objects.filter(film=film)

    if request.method == 'POST':
        form_opinia = OpiniaForm(request.POST)
        form_ocena = OcenaForm(request.POST)
        if form_opinia.is_valid() and form_ocena.is_valid():
            opinia = form_opinia.save(commit=False)
            opinia.film = film
            opinia.recenzent = Recenzent.objects.get(user=request.user)
            opinia.save()

            ocena = form_ocena.save(commit=False)
            ocena.opinia = opinia
            ocena.save()

            return redirect('opinia_ocena', film_id=film.id)

    else:
        form_opinia = OpiniaForm()
        form_ocena = OcenaForm()

    return render(request, 'opinia_ocena.html', {'form_opinia': form_opinia, 'form_ocena': form_ocena, 'opinie': opinie})


def rejestracja_recenzenta(request):
    if request.method == "POST":
        form = RejestracjaRecenzentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RejestracjaRecenzentaForm()
    return render(request, 'rejestracja.html', {'form': form})


def wszystkie_opinie(request):
    """
    Widok wyświetlający wszystkie opinie dla wszystkich filmów.
    """
    opinie = Opinia.objects.all()

    return render(request, 'wszystkie_opinie.html', {'opinie': opinie})


@login_required
def profile(request):
    """
    Wyświetla profil recenzenta
    """
    recenzent = request.user.recenzent
    return render(request, 'profile.html', {'recenzent': recenzent})
