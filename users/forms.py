from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

class LoginForm(forms.Form):
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        
        try :
            user = models.User.objects.get(username=email)

            if user.check_password(password) :
                return self.cleaned_data
            else :
                self.add_error('password', forms.ValidationError('Password is wrong'))
        except models.User.DoesNotExist :
            self.add_error('email', forms.ValidationError('User does not exist'))


class SignUpForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = ("first_name", "last_name", "email")

        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last Name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email Name"}),
        }
    
    password = forms.CharField(
        widget = forms.PasswordInput(attrs={"placeholder": "Password"})
    )

    password1 = forms.CharField(
        widget = forms.PasswordInput(attrs={"placeholder": "Confirm Password"})
    )

    def clean_password1(self):
        password = self.cleaned_data.get("password")