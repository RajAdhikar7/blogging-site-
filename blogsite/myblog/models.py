from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Inherit from AbstractUser to get default user fields like username, password, etc.
    TYPE_CHOICES = (
        ('author', 'Author'),
        ('reader', 'Reader'),
    )
    user_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='reader')
    

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_type': 'author'})  # Restrict authors
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)  # Optional category
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_type': 'reader'})  # Restrict to readers
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
