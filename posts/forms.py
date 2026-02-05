from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post


# Register Form
#👉 Uses Django built-in secure user system
#👉 Automatically hashes passwords
class RegisterForm(UserCreationForm):
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
