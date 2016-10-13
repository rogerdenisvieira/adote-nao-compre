from django.forms import ModelForm
from django.contrib.auth.models import User
from AdoteNaoCompreSITE.models.dog import Dog
from django import forms


class DogForm(ModelForm):
    class Meta:
        model = Dog
        fields = "__all__"
        exclude = ["IdProtetor","Interesse"]

        labels = {
            'DataRegistro': ('Data de Registro'),
            'Info': ('Informações')
        }


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
    
    #username = forms.CharField()
    #password = forms.PasswordInput

    labels = {
        'username': ('Usuário'),
        'password': ('Senha')
    }


class SearchDogForm(ModelForm):
    class Meta:
        model = Dog
        fields = ["Sexo", "Idade"]


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password", "email"]

        labels = {
            'username': ('Usuário'),
            'first_name':('Nome'),
            'last_name': ('Sobrenome'),
            'password': ('Senha'),
            'email': ('Email')
        }
