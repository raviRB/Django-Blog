from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Posts, Comments, Reply, Blog_detail, User_Profile
from django.contrib.auth.models import User


class NewPostForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Post Body ...'}), max_length=4000)
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Post Heading ...'}))

    class Meta:
        model = Posts
        fields = ['title', 'body']

class NewCommentForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write your message here ...'}), max_length=1000)
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email Address'}), max_length=100)
    user_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full Name'}), max_length=100)

    class Meta:
        model = Comments
        fields = ['user_name', 'email' , 'message']

class NewReplyForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write your message here ...'}), max_length=1000)
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email Address'}), max_length=100)
    user_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full Name'}), max_length=100)

    class Meta:
        model = Reply
        fields = ['user_name', 'email' , 'message']

class AdminLogin(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}) , required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}), required=True)


class AccountDetail(forms.ModelForm):

    class Meta:
        model = User_Profile
        fields = ('username', 'email', 'password', 'about_user', 'profile_link', 'blog_name', 'profile_pic')


class SignUpForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}))

    class Meta:
        model = User_Profile
        fields = ('username', 'email', 'password','about_user','profile_link','blog_name')

