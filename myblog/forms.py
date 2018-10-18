from django import forms
from .models import Posts, Comments


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

class AdminLogin(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
