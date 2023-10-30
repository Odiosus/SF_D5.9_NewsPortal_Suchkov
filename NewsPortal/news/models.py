# импортировали встроенную модель Пользователь
from django.contrib.auth.models import User
# импортировали модели Django
from django.db import models
# импортировали Sum
from django.db.models import Sum
# импортировали функцию
from django.db.models.functions import Coalesce


# Create your models here.
# модель Автор
class Author(models.Model):
    # связь 1к1 со встроенной моделью User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # поле с рейтингом автора
    rating = models.IntegerField(default=0)

    # метод обновления рейтинга автора, ломающий судьбы начинающих программистов
    def update_rating(self):
        # считаем рейтинг постов автора
        posts_rating = self.posts.aggregate(pr=Coalesce(Sum('rating'), 0)).get('pr')
        # считаем рейтинг комментариев
        comments_rating = self.user.comments.aggregate(cr=Coalesce(Sum('rating'), 0)).get('cr')
        # считаем рейтинг комментариев к постам
        posts_comments_rating = self.posts.aggregate(pcr=Coalesce(Sum('comment__rating'), 0)).get('pcr')

        # умножаем и складываем рейтинги
        self.rating = posts_rating * 3 + comments_rating + posts_comments_rating
        # сохранились
        self.save()


# модель Категории
class Category(models.Model):
    # поле с именем категории, уникальное. Не более 30 символов
    name = models.CharField(max_length=30, unique=True)


# модель Новости
class Post(models.Model):
    # переменные модели Новость (разделы: новость или статья)
    news = 'N'
    article = 'A'

    # красиво отображаем переменные разделов новостей
    SECTION = [
        (news, "Новость"),
        (article, "Статья")
    ]

    # связь 1к2 с моделью Автор
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    # выбираем раздел поста: новость/статья
    section = models.CharField(max_length=1, choices=SECTION)
    # заголовок поста
    heading = models.CharField(max_length=255)
    # текст поста
    text = models.TextField()
    # дата и время создания поста, полностью автоматизированное
    post_time = models.DateTimeField(auto_now_add=True)
    # рейтинг поста
    rating = models.IntegerField(default=0)
    # связь 1к2 с моделью Категории через модель PostCategory
    category = models.ManyToManyField(Category, through='PostCategory')

    # считаем лайки поста
    def like(self):
        # посчитали лайки поста
        self.rating += 1
        # сохранились
        self.save()

    # считаем дизлайки поста
    def dislike(self):
        # посчитали дизлайки поста
        self.rating -= 1
        # сохранились
        self.save()

    # делаем превью поста
    def preview(self):
        # установили длину превью в 124 символа + многоточие
        return self.text[:124] + '...'


# связь моделей Новость и Категория
class PostCategory(models.Model):
    # связь 1к2 с моделью Новость
    post_in = models.ForeignKey(Post, on_delete=models.CASCADE)
    # связь 1к2 с моделью Категория
    in_category = models.ForeignKey(Category, on_delete=models.CASCADE)


# модель Комментарий
class Comment(models.Model):
    # связь 1к2 с моделью Новость
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # связь с моделью User
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    # текст комментария, никаких ограничений — даем волю чувствам
    text = models.TextField()
    # дата и время создания комментария, полностью автоматизированное
    comment_time = models.DateTimeField(auto_now_add=True)
    # рейтинг комментария
    rating = models.IntegerField(default=0)

    # считаем лайки комментария
    def like(self):
        # посчитали лайки комментария
        self.rating += 1
        # сохранились
        self.save()

    # считаем дизлайки комментария
    def dislike(self):
        # посчитали дизлайки комментария
        self.rating -= 1
        # сохранились
        self.save()
