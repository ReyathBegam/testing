from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post


# Register Form
#👉 Uses Django built-in secure user system
#👉 Automatically hashes passwords
class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150, help_text='')  # remove default help text
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        help_text=''  # remove default password rules text
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput,
        help_text=''  # remove default confirm password text
    )
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


# Photo Upload Form
#👉 Creates form from your Post model
#👉 Includes image + caption
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'caption']
