# Generated by Django 2.1.2 on 2018-10-15 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20181009_0811'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_name', models.CharField(max_length=20)),
                ('admin_name', models.CharField(max_length=50)),
                ('about_admin', models.CharField(max_length=250)),
                ('profile_link', models.CharField(max_length=1000)),
                ('image', models.ImageField(blank=True, upload_to='profile_picture')),
            ],
        ),
    ]
