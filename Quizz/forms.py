from django import forms

class UserForm(forms.Form):
    login = forms.CharField(label='login', max_length=255)
    mail = forms.EmailField(label='mail', max_length=255)
    password = forms.CharField(label='password', max_length=255, widget=forms.PasswordInput)

