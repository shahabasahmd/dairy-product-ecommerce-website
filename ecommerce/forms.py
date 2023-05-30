from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from .models import Customer



class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'locality', 'city', 'mobile', 'zipcode')

 