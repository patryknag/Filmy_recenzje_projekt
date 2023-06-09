"""
URL configuration for Filmy_projekt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from filmy_app import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('gatunki_filmy/', views.gatunki_filmy, name='gatunki_filmy'),
    path('film/<int:pk>/', views.film, name='film'),
    path('opinia_ocena/<int:film_id>/', views.opinia_ocena, name='opinia_ocena'),
    path('rejestracja/', views.rejestracja_recenzenta, name='rejestracja'),
    path('wszystkie_opinie/', views.wszystkie_opinie, name='wszystkie_opinie'),
    path('accounts/profile/', views.profile, name='profile')

]
