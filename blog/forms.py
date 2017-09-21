from django import forms

class RegistroUsuarios(forms.Form):
    nombre = forms.CharField(max_length=150)
    apellido1 = forms.CharField(max_length=150)
    apellido2 = forms.CharField(max_length=150)
    email = forms.EmailField()
    telefono = forms.IntegerField()

    def __str__(self):
        return '{0} {1}'.format(self.nombre, self.email)