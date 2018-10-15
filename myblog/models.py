from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=100 , null=False)
    body = models.CharField(max_length=4000 , null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comments(models.Model):
    user_name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    message = models.CharField(max_length=1000, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Posts, related_name='comment', on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name

class Blog_detail(models.Model):
    blog_name = models.CharField(max_length=20 , null=False)
    admin_name = models.CharField(max_length=50 , null=False)
    about_admin = models.CharField(max_length=250, null=False)
    profile_link = models.CharField(max_length=1000, null=False)
    image = models.ImageField(upload_to="profile_picture",blank=True)
