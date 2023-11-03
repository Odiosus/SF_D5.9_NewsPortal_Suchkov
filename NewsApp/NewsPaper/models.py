from django.db import models


# Create your models here.
# модель Новость
class News(models.Model):
    # заголовок новости (уникальный заголовок исключит повторную публикацию новости)
    heading = models.CharField(max_length=100, unique=True)
    # текст новости (уникальный текст исключит повторную публикацию новости)
    text = models.TextField(unique=True)
    # поле категории ссылается на модель категории
    # все новости в категории будут доступны через поле news
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='news')
    # ⚠️поле автор новости
    author = models.CharField(max_length=255)

    def __str__(self):
        # почикали админку
        return f'{self.heading.title()}: {self.text[:20]}'


# Модель Категория, к которой будет привязываться новость
class Category(models.Model):
    # названия категорий уникальное
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name.title()