from django.contrib.auth.models import AbstractUser
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    POST_STATUS = (
        ('n', 'Новая'),
        ('a', 'Принято в работу'),
        ('d', 'Выполнено')

    )

    status = models.CharField(max_length=1, choices=POST_STATUS, default='n')
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-creation_date']

class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
