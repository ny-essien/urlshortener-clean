from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Link

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class LinkCreateForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['original_url']
        widgets = {
            'original_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your long URL here...'
            })
        } 