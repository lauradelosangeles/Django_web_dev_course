from django import forms


class ContactoForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        label='Tu nombre',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre completo'}),
    )
    correo = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'tu@correo.com'}),
    )
    mensaje = forms.CharField(
        label='Mensaje',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Escribe tu mensaje aquí...'}),
    )


class ContactoFormEN(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        label='Your name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your full name'}),
    )
    correo = forms.EmailField(
        label='Email address',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'you@email.com'}),
    )
    mensaje = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Write your message here...'}),
    )
