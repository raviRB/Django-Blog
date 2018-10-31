import os
from django.shortcuts import render, redirect
from .models import Posts, Comments, Reply, User_Profile
from .forms import NewPostForm, NewCommentForm, NewReplyForm, AccountDetail, SignUpForm, AdminLogin
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User

# user object define the username of the blog admin
# requrest.user is the user who requested for the page

def first_page(request,user):
    a = User.objects.filter(username=user).count()
    if a==0:
        raise Http404("No such User Exists")
    else:
        blog_admin = User.objects.get(username=user)
        user_detail = blog_admin.profile
        all_posts = blog_admin.my_post.all()
        posts_2 = []

        if len(all_posts) <= 2:
            posts_2 = all_posts
        else:
            for i in range(0, 2):
                posts_2.append(all_posts[i])
        return render(request, 'index.html', {'all_posts': all_posts, 'posts_2': posts_2, 'user_detail': user_detail ,'blog_admin':user})


def new_post(request,user):
    if not request.user.is_authenticated:
        return  redirect('login' )
    user_detail = request.user.profile
    if request.method =="POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
        return redirect('first_page', user=user)
    else:
        form = NewPostForm()
        return render(request, 'new_post.html', {'form':form , 'user_detail':user_detail , 'blog_admin':user})


def specific_post(request , post_id,user):
    blog_admin = User.objects.get(username=user)
    all_posts = blog_admin.my_post.all()
    requested_post = blog_admin.my_post.get(pk=post_id)
    user_detail = blog_admin.profile
    form = NewCommentForm()
    reply_form = NewReplyForm()
    if request.method =="POST":
        form = NewCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = requested_post
            comment.save()
            return redirect('specific_post',post_id=post_id, blog_admin=user)

    return render(request, 'post_detail.html', {'post': requested_post, 'all_posts': all_posts ,'form':form ,'user_detail':user_detail ,'reply_form':reply_form ,'blog_admin':user})


def all_post(request,user):
    blog_admin = User.objects.get(username=user)
    all_posts = blog_admin.my_post.all()
    user_detail = blog_admin.profile
    return render(request, 'all_posts.html', {'all_posts': all_posts , 'user_detail':user_detail,'blog_admin':user})


def logout_user(request):
    logout(request)
    return redirect('home')


def comment(request,comment_id,user):
    requested_comment = Comments.objects.get(pk=comment_id)
    if request.method == "POST":
        form = NewReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.comment = requested_comment
            reply.save()
    return redirect(request.META['HTTP_REFERER'])


def setting(request,user):
    if not request.user.is_authenticated:
        return redirect('login')
    blog_admin = request.user
    user_detail = blog_admin.profile
    if request.method == "POST":
        form = AccountDetail(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            if len(request.FILES) == 0:
                profile.profile_pic = user_detail.profile_pic
            else:
                user_detail.profile_pic.delete()
            profile.user = user_detail.user
            profile.password = user_detail.password
            profile.pk = user_detail.pk
            profile.save(force_update=True)
            return redirect('first_page', user=user)

    else:
        form = AccountDetail(
            initial={'email': user_detail.email, 'username': user_detail.username, 'about_user': user_detail.about_user,
                     'blog_name': user_detail.blog_name,
                     'profile_link': user_detail.profile_link,
                     'profile_pic': user_detail.profile_pic})
    all_posts = blog_admin.my_post.all()
    return render(request, 'setting.html',
                  {'all_posts': all_posts, 'user_detail': user_detail, 'form': form, 'blog_admin': user})


def edit_post(request,post_id,user):
    if not request.user.is_authenticated:
        return redirect('login')
    blog_admin = request.user
    user_detail = blog_admin.profile
    post = blog_admin.my_post.get(pk=post_id)
    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            my_post = form.save(commit=False)
            my_post.pk = post_id
            my_post.created_on = post.created_on
            my_post.updated_on = datetime.now()
            my_post.save(force_update=True)
        return redirect('first_page', user=user)
    else:
        form = NewPostForm(initial={'title': post.title, 'body': post.body})
        return render(request, 'edit_post.html', {'form': form, 'post': post, 'user_detail': user_detail, 'blog_admin':user})


def delete_comment(request,comment_id,user):
    if not request.user.is_authenticated:
        return redirect('first_page', user=user)
    Comments.objects.filter(id=comment_id).delete()
    return redirect(request.META['HTTP_REFERER'])


def delete_reply(request,reply_id,user):
    if not request.user.is_authenticated:
        return redirect('first_page', user=user)
    Reply.objects.filter(id=reply_id).delete()
    return redirect(request.META['HTTP_REFERER'])


def delete_post(request,post_id,user):
    if not request.user.is_authenticated:
        return redirect('first_page', user=user)
    Posts.objects.filter(id=post_id).delete()
    return redirect('settings')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            a = int(User.objects.filter(username=data.username).count())
            if a > 0:
                messages.warning(request, 'Username already exists', extra_tags='alert')
            else:
                user = User.objects.create_user(username=data.username,
                                                email=data.email,
                                                password=data.password)
                user.save()
                data.user = user
                data.save()
                return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def home(request):
    profiles = User_Profile.objects.all()
    if request.user.is_authenticated:
        return redirect('first_page', request.user.username)
    if request.method =="POST":
        form = AdminLogin(request.POST)
        if form.is_valid():
            username  = form.cleaned_data['username']
            password  = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('first_page', user=username)
            else:
                messages.warning(request, 'Invalid Username or Password', extra_tags='alert')
    else:
        form = AdminLogin()
    return render(request, 'home.html', {'form': form , 'profiles':profiles})