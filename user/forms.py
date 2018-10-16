from django import forms

class LoginForm(forms.Form):
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "First Name"}))
    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Last Name"}))
    email = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Email"}))
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': "Password"}))
    confirm_password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': "Confirm password"}))
