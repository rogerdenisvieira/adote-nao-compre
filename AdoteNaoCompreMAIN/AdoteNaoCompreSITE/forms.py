from django.forms import ModelForm
from django.contrib.auth.models import User
from AdoteNaoCompreSITE.models.dog import Dog
from django import forms


class DogForm(ModelForm):
    class Meta:
        model = Dog
        fields = "__all__"
        exclude = ["IdProtetor","Interesse"]

        error_messages = {
            'Nome': {
                'required': ("This writer's name is too long."),
            }
        }

class LoginForm(forms.Form):
    username = forms.TextInput()
    password = forms.PasswordInput()


class SearchDogForm(ModelForm):
    class Meta:
        model = Dog
        fields = ["Sexo", "Idade"]


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password", "email"]

        labels = {
            'username': ('Usu�rio'),
            'first_name':('Nome'),
            'last_name': ('Sobrenome'),
            'password': ('Senha'),
            'email': ('Email')
        }
