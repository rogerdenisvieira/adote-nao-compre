from django.forms import ModelForm, ModelChoiceField
from django.contrib.auth.models import User
from AdoteNaoCompreSITE.models.dog import Dog
from AdoteNaoCompreSITE.models.breed import Breed
from django import forms


class DogForm(ModelForm):
    class Meta:
        model = Dog
        fields = "__all__"
        exclude = ["IdProtetor","Interesse"]
        breed = ModelChoiceField(queryset= Breed.objects.all(), empty_label='')

        labels = {
            'DataRegistro': ('Data de Registro'),
            'Info': ('Informações'),
            'IdRaca': ('Raça')
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