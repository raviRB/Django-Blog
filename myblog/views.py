import os
from django.shortcuts import render, redirect
from .models import Posts, Blog_detail, Comments
from .forms import NewPostForm, NewCommentForm, AdminLogin, NewReplyForm, AccountDetail
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from datetime import datetime

def first_page(request):
    blog_detail = Blog_detail.objects.get(pk=1)
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

    return render(request,'index.html',{'all_posts':all_posts , 'posts_2':posts_2 , 'form_login':form_login , 'blog_detail':blog_detail})


def new_post(request):
    blog_detail = Blog_detail.objects.get(pk=1)
    if request.method =="POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
        return redirect('first_page')
    else:
        form = NewPostForm()
        return render(request, 'new_post.html', {'form':form , 'blog_detail':blog_detail})


def specific_post(request , post_id):
    requested_post = Posts.objects.get(pk=post_id)
    blog_detail = Blog_detail.objects.get(pk=1)
    if request.method =="POST":
        form = NewCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = requested_post
            comment.save()

        return redirect(request.META['HTTP_REFERER'])
    else:
        form = NewCommentForm()
        reply_form = NewReplyForm()
        form_login = AdminLogin()
        all_posts = Posts.objects.all()
        return render(request, 'post_detail.html', {'post': requested_post, 'all_posts': all_posts ,'form':form , 'form_login':form_login , 'blog_detail':blog_detail ,'reply_form':reply_form})


def all_post(request):
    blog_detail = Blog_detail.objects.get(pk=1)
    all_posts = Posts.objects.all()
    form_login = AdminLogin()
    return render(request, 'all_posts.html', {'all_posts': all_posts , 'form_login':form_login , 'blog_detail':blog_detail})


def logout_user(request):
    logout(request)
    return redirect('first_page')


def comment(request,comment_id):
    requested_comment = Comments.objects.get(pk=comment_id)
    if request.method == "POST":
        form = NewReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.comment = requested_comment
            reply.save()
    return redirect(request.META['HTTP_REFERER'])


def setting(request):
    if  not request.user.is_authenticated:
        request('first_page')
    blog_detail = Blog_detail.objects.get(pk=1)
    if request.method =="POST":
        form = AccountDetail(request.POST,request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            if not comment.image:
                comment.image = blog_detail.image
            else:
                blog_detail.image.delete()
            comment.pk=1
            comment.save(force_update=True)

        return redirect('first_page')
    else:
        all_posts = Posts.objects.all()
        form = AccountDetail(initial={'admin_name': blog_detail.admin_name, 'about_admin': blog_detail.about_admin,
                                      'blog_name': blog_detail.blog_name,
                                      'profile_link': blog_detail.profile_link, 'image': blog_detail.image})
        return render(request, 'setting.html', {'all_posts': all_posts, 'blog_detail': blog_detail, 'form': form})


def edit_post(request,post_id):

    blog_detail = Blog_detail.objects.get(pk=1)
    post = Posts.objects.get(pk=post_id)
    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            my_post = form.save(commit=False)
            my_post.pk = post_id
            my_post.created_on = post.created_on
            my_post.updated_on = datetime.now()
            my_post.save(force_update=True)
        return redirect('first_page')
    else:
        form = NewPostForm(initial={'title':post.title ,'body':post.body})
        return render(request, 'edit_post.html', {'form': form, 'post': post , 'blog_detail':blog_detail})
