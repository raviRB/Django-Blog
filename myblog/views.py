from django.shortcuts import render, redirect
from .models import Posts
from .forms import NewPostForm, NewCommentForm, AdminLogin
from django.contrib.auth import authenticate, login, logout
from django.http import Http404

def first_page(request):
    all_posts = Posts.objects.all()
    posts_2 = []

    if len(all_posts)<=2:
        posts_2=all_posts
    else:
        for i in range(0,2):
            posts_2.append(all_posts[i])
    form_login = AdminLogin()

    if request.method =="POST":
        form = AdminLogin(request.POST)
        if form.is_valid():
            username  = form.cleaned_data['username']
            password  = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(request.META['HTTP_REFERER'])
            else:
                raise Http404("Invalid Username or Password")

    return render(request,'index.html',{'all_posts':all_posts , 'posts_2':posts_2 , 'form_login':form_login})


def new_post(request):
    if request.method =="POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
        return redirect('first_page')
    else:
        form = NewPostForm()
        return render(request, 'new_post.html', {'form':form})


def specific_post(request , post_id):
    requested_post = Posts.objects.get(pk=post_id)
    if request.method =="POST":
        form = NewCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = requested_post
            comment.save()
        return redirect(request.META['HTTP_REFERER'])
    else:
        form = NewCommentForm()
        form_login = AdminLogin()
        all_posts = Posts.objects.all()
        return render(request, 'post_detail.html', {'post': requested_post, 'all_posts': all_posts ,'form':form , 'form_login':form_login })


def all_post(request):
    all_posts = Posts.objects.all()
    form_login = AdminLogin()
    return render(request, 'all_posts.html', {'all_posts': all_posts , 'form_login':form_login})


def logout_user(request):
    logout(request)
    return redirect(request.META['HTTP_REFERER'])