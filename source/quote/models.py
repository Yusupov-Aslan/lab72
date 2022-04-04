from django.db import models


# Create your models here.
CHOICES = [("new", "Новая"), ("approved", "Модерированная"), ]


class Quote(models.Model):
    text = models.TextField(max_length=2000, verbose_name="Текст")
    user_name = models.CharField(max_length=256, verbose_name='Имя добавившего')
    email = models.EmailField(verbose_name='Эл. адрес')
    rating = models.PositiveIntegerField(default=0, verbose_name='Рейтинг')
    status = models.CharField(max_length=24, choices=CHOICES, default='new', verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
