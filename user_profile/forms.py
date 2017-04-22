from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            try:
                user = User.objects.get(username=username)
                user = authenticate(username=username, password=password)
                if not user:
                    raise forms.ValidationError(
                        'Username or password incorrect!')
                if not user.is_active:
                    raise forms.ValidationError('User no longer active!')
            except User.DoesNotExist:
                raise forms.ValidationError('User does not exist!')


class UserRegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100,
                                 label='First Name')
    last_name = forms.CharField(max_length=100,
                                label='Last Name')
    email = forms.EmailField(max_length=100,
                             label='Email')
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput,
                                       label='Confirm Password')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Username %(username)s is already in use!',
                                    params={'username': username})

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Passwords do not match!')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password', 'confirm_password']
