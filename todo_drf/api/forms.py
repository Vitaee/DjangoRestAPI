from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label = "Kullanıcı Adı")
    password = forms.CharField(label = "Parola",widget = forms.PasswordInput)
    token = forms.CharField(max_length=200, label="Token")

