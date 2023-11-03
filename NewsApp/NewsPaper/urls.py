# ✅создали файл самостоятельно и импортировали пути
from django.urls import path
# Импортируем созданное нами представление
# ✅DetailView. Он отличается от ListView тем, что возвращает конкретный объект, а не список всех объектов из БД
from .views import NewsList, NewsDetail


urlpatterns = [
    # path — путь.
    # путь ко всем новостям остаётся пустым
    # объявленное представление является классом — представляем этот класс в виде view
    # вызываем метод as_view.
    path('', NewsList.as_view()),
    # добавили для работы не через pk, а через id (NewsPaper/urls.py). Настройка лежит в views.py (pk_url_kwarg = 'id')
    path('<int:id>', NewsDetail.as_view()),
]
