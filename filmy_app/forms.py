from django import forms
from .models import Opinia, Ocena, Recenzent
from django.contrib.auth.models import User


class OpiniaForm(forms.ModelForm):
    class Meta:
        model = Opinia
        fields = ['text']


class OcenaForm(forms.ModelForm):
    class Meta:
        model = Ocena
        fields = ['ocena']


class RejestracjaRecenzentaForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput(), label="Potwierdź hasło")

    class Meta:
        model = Recenzent
        fields = ['name', 'surname']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("password_confirm")

        if password != confirm_password:
            self.add_error('password_confirm', "Hasła nie są takie same")

    def save(self, *args, **kwargs):
        user = User.objects.create_user(self.cleaned_data['username'], password=self.cleaned_data['password'])
        recenzent = Recenzent.objects.create(user=user, name=self.cleaned_data['name'], surname=self.cleaned_data['surname'])
        return recenzent
