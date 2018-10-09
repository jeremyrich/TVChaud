from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="", max_length=30, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Email", 'disabled': 'disabled'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': "Password", 'disabled': 'disabled'}))
