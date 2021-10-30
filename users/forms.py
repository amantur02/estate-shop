from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Profile


class ProfileRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Profile
        fields = UserCreationForm.Meta.fields + ('phone',)


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'phone', 'email', 'image']
