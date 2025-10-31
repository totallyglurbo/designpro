from django.db import models
from django.contrib.auth.models import AbstractUser

class ReallyUser(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True)
    agreement = models.BooleanField(default=False, verbose_name='Приняли соглашение?')

    class Meta(AbstractUser.Meta):
        pass

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
