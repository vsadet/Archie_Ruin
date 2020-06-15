from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(max_length=2)


class Blog(models.Model):
    start_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    topic = models.CharField(max_length=30, null=True)


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    topic = models.CharField(max_length=30, null=True)
