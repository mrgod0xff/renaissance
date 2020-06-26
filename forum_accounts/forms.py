from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )


User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
       
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Cet utilisateur n'existe pas")
            if not user.check_password(password):
                raise forms.ValidationError("Mot de passe incorrect")
            if not user.is_active:
                raise forms.ValidationError("Cet utilisateur n'est plus actif.")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Adresse électronique')
    password = forms.CharField(widget=forms.PasswordInput, label='Mot de passe')
    username = forms.CharField(label='Pseudo')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]
