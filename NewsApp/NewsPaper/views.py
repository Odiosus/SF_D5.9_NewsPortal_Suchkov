# Create your views here.
# ✅импорт модуль datetime — получаем текущую дату
from datetime import datetime
# ✅импорт дженериков ListView, DetailView
from django.views.generic import ListView, DetailView
# импорт модели News
from .models import News
# ❇️можно поглядеть в def get_context_data(self, **kwargs):
# from pprint import pprint
# Create your views here.


# Тут смотрим новости – news
class NewsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = News
    # сортируем через наоборот
    ordering = '-id'
    # Имя шаблона для новостей — News
    template_name = 'news.html'
    # Имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'

    # Метод get_context_data позволяет изменить набор данных, который будет передан в шаблон.
    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        # ✅доп переменная анонс (announcement) статей (их правда пока нет, но они будут)
        context['announcement'] = None
        return context


# Тут смотрим конкретную новость – one_news
class NewsDetail(DetailView):
    # модель для получения информации по отдельной новости
    model = News
    # используем новый шаблон — one_news.html
    template_name = 'one_news.html'
    # название объекта, в котором будет выбранная статья
    context_object_name = 'one_news'
    # добавили для работы не через pk, а через id (NewsPaper/urls.py)
    pk_url_kwarg = 'id'

