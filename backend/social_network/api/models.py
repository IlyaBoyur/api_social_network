from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models

MEN = 'M'
WOMEN = 'W'
GENDER_CHOICES = (
    (MEN, 'Мужской'),
    (WOMEN, 'Женский'),
)


class User(AbstractUser):
    phone = models.PositiveIntegerField(
        'Номер телефона',
        unique=True,
    )
    email = models.EmailField(
        'Электронная почта',
        unique=True,
    )
    about = models.TextField(
        'О себе',
        max_length=500,
    )
    gender = models.CharField(
        'Пол',
        max_length=1,
        choices=GENDER_CHOICES,
    )
    age = models.PositiveSmallIntegerField(
        'Возраст',
        validators=(
            validators.MinValueValidator(7, 'Минимальный возраст: 7'),
        ),
    )
    register_date = models.DateTimeField(
        'Дата регистрации',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'[{self.username}: {self.phone}; {self.email}]'


class Post(models.Model):
    text = models.TextField(
        'Текст',
        max_length=500,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор',
    )
    pub_date = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = (
            '-pub_date',
        )

    def __str__(self):
        return f'[{self.author.username}] {self.text[:50]}'


class PostImage(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Пост',
    )
    image = models.ImageField(
        'Изображение',
        upload_to='posts',
    )
