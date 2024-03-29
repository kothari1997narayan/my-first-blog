from django import forms

from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class LoginForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1')

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'image_post',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)