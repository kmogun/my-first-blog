from django import forms
from registration.forms import RegistrationForm

class RegistroUsuarios(forms.Form):
    nombre = forms.CharField(max_length=150, label='Tu nombre:')
    apellido1 = forms.CharField(max_length=150, label='Tu apellido:')
    apellido2 = forms.CharField(max_length=150, label='Tu segundo apellido:')
    email = forms.EmailField(label='Tu e-mail:')
    telefono = forms.IntegerField(label='Tu telefono:')

    def __str__(self):
        return '{0}'.format(self.email)