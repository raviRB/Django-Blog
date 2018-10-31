from django.db import models
from django.contrib.auth.models import User


class Posts(models.Model):
    user = models.ForeignKey(User,related_name="my_post",on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=100 , null=False)
    body = models.CharField(max_length=4000 , null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title +" "+str(self.pk)

class Comments(models.Model):
    user_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    message = models.CharField(max_length=1000, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Posts, related_name='comment', on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name+" "+str(self.pk)

class Reply(models.Model):
    user_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    message = models.CharField(max_length=1000, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comments, related_name='reply', on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name+" "+str(self.pk)

class Blog_detail(models.Model):
    admin_name = models.CharField(max_length=50 , null=False)
    about_admin = models.CharField(max_length=250, null=False)
    blog_name = models.CharField(max_length=20, null=False)
    profile_link = models.CharField(max_length=1000, null=False)
    image = models.ImageField(upload_to="profile_picture/",blank=True)

    def __str__(self):
        return self.admin_name+" "+str(self.pk)


class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , related_name='profile')
    username = models.CharField(max_length=254, null=False)
    password = models.CharField(max_length=254, null=False)
    email = models.EmailField(max_length=254, null=False)
    about_user = models.CharField(max_length=254, null=False)
    blog_name = models.CharField(max_length=254, null=False)
    profile_link = models.CharField(max_length=254, null=False)
    profile_pic = models.ImageField(upload_to="profile_picture/",blank=True , default='default/avatar.png')

    def __str__(self):
        return self.username + " " + str(self.pk)