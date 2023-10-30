# пошли в shell
>>> python manage.py shell
# импортировали модели в приложение news
>>> from news.models import *

# встречаем первых трёх пользоватлей
>>> u1 = User.objects.create_user(username='Alex')
>>> u2 = User.objects.create_user(username='Ivan')
>>> u3 = User.objects.create_user(username='Alisa')

# приветствуем первых двух авторов, пришедших из пользователей
>>> a1 = Author.objects.create(user=u1)
>>> a2 = Author.objects.create(user=u2)

# Запустили раздел Политика (c1 - вытаскиваем через get после выхода из shell)
>>> politics = Category.objects.create(name="Политика")
# Запустили раздел Экономика (c2 - вытаскиваем через get после выхода из shell)
>>> economic = Category.objects.create(name="Экономика")
# Запустили раздел Криминал (c3 - вытаскиваем через get после выхода из shell)
>>> criminal = Category.objects.create(name="Криминал")
# Запустили раздел Культура (c4 - вытаскиваем через get после выхода из shell)
>>> culture = Category.objects.create(name="Культура")
# Запустили раздел АйТи (c5 - вытаскиваем через get после выхода из shell)
>>> it = Category.objects.create(name="АйТи")
# Сообщили миру новость № 1 от автора № 1
>>> n1 = Post.objects.create(author=a1,
                                 section = "N",
                                 heading = "Первый канал берет новые вершины",
                                 text = "Первый канал берет новые вершины: рассказ единоросски Бутиной об "
                                 "очередном коварстве Америки сопровождает танцующий актер в костюме инопланетянина.")
# Сообщили миру новость № 2 от автора № 2
>>> n2 = Post.objects.create(author=a2,
                                 section = "N",
                                 heading = "Умер экс-глава правительства Китая Ли Кэцян. В китайских соцсетях "
                                 "резко выросла популярность песни «Sorry it wasnʼt you» («Жаль, что не ты») — "
                                 "с намеком на Си Цзиньпина",
                                 text = "26 октября у 68-летнего Ли Кэцяна произошел сердечный приступ. "
                                 "Несмотря на все усилия врачей, спаси его не удалось, цитирует Reuters сообщение, "
                                 "переданное в эфире китайского телеканала CCTV. В связи со смертью Ли Кэцяна некоторые "
                                 "сайты госорганов сменили оформление на траурное, а соцсеть Weibo заменила отметку "
                                 "«Нравится» на «Скорблю». Ли Кэцян занимал пост премьера Госсовета — главы правительства "
                                 "Китая — с 2013 года. Он покинул его в марте 2023 года, когда председатель "
                                 "КНР Си Цзиньпин провел кадровые изменения в ряде госструктур. "
                                 "Ли Кэцян считался сторонниом экономических реформ и свободного рынка, напоминает Reuters. "
                                 "Независимый китайский политический аналитик Адам Ни описал его как «премьера, который "
                                 "оказался бессильным, когда Китай резко свернул от реформ и открытости». "
                                 "Тем не менее, отмечает Reuters, представители либеральных кругов, "
                                 "обсуждая смерть Ли Кэцяна в соцсети WeChat, говорили об этом как о конце эпохи. "
                                 "После смерти Ли Кэцяна в китайских соцсетях резко выросла популярность "
                                 "песни «Sorry it wasnʼt you» («Жаль, что не ты»), которую пользователи упоминали, "
                                 "намекая на действующего главу Китая Си Цзиньпина. "
                                 "Такой же всплеск популярности у этой композиции был в ноябре 2022 года, "
                                 "когда умер бывший председатель КНР Цзян Цзэминь.")
# Автор № 1 разместил статью № 1
>>> ar1 = Post.objects.create(author=a1,
                                   section = "A",
                                   heading = "Аргументы. ForeignKey принимает другие аргументы, "
                                   "которые определяют детали работы отношений.",
                                   text = "ForeignKey.on_delete. При удалении объекта, на который ссылается ForeignKey, "
                                   "Django будет эмулировать поведение ограничения SQL, заданного аргументом "
                                   "on_delete. Например, если у вас есть обнуляемым ForeignKey и вы хотите, "
                                   "чтобы он был установлен в null, когда ссылочный объект удален. "
                                   "Возможные значения для on_delete находятся в django.db.models. "
                                   "CASCADE. Каскадное удаление. Django эмулирует поведение ограничения "
                                   "SQL ON DELETE CASCADE, а также удаляет объект, содержащий ForeignKey. "
                                   "Model.delete() не вызывается в связанных моделях, но сигналы pre_delete и post_delete "
                                   "отправляются для всех удаленных объектов. "
                                   "PROTECT. Предотвращает удаление объекта, на который есть ссылка, путем вызова ProtectedError, "
                                   "подкласса django.db.IntegrityError. "
                                   "RESTRICT. Предотвращает удаление указанного объекта путем вызова RestrictedError "
                                   "(подкласс django.db.IntegrityError). В отличие от PROTECT, удаление ссылочного объекта допускается, "
                                   "если он также ссылается на другой объект, который удаляется в той же операции, но через отношение CASCADE. "
                                   "SET_DEFAULT. Устанавливает для ForeignKey значение по умолчанию; "
                                   "значение по умолчанию для ForeignKey должно быть указано в описании поля.")
# Автор № 2 разместил статью № 2
>>> ar2 = Post.objects.create(author=a2,
                                   section = "A",
                                   heading = "❗️Центробанк поднял ключевую ставку сразу до 15% годовых",
                                   text = "Рост составил два процентных пункта, сообщает ТАСС. На этом фоне курс доллара опустился ниже 93 рубля. "
                                   "На сайте ЦБ сообщается, что инфляция складывается выше ожиданий Центробанка, "
                                   "а увеличение внутреннего спроса «все больше превышает возможности расширения производства товаров и услуг». "
                                   "Также, согласно сообщению ЦБ, в России «остаются высокими темпы роста кредитования». "
                                   "«В этих условиях требуется обеспечить дополнительное ужесточение денежно-кредитной политики "
                                   "для ограничения масштаба отклонения инфляции вверх от цели и ее возвращения к 4% в 2024 году», — сообщает Центробанк. "
                                   "Банк России прогнозирует по итогам 2023 года годовую инфляцию в диапазоне 7,0-7,5%. "
                                   "Предполагается, что повышение ставки позволит снизить инфляцию до 4,0-4,5% в 2024 году и сохранить ее около 4% в будущем. "
                                   "Последний раз регулятор поднимал ставку рефинансирования в сентябре с 12% до 13%.")

# Добавили 2 категории к новости № 1
>>> n1.category.add(criminal)
>>> n1.category.add(culture)
# Добавили 2 категории к новости № 2
>>> n2.category.add(politics)
>>> n2.category.add(criminal)
# Добавили 1 категорию к статье № 1
>>> ar1.category.add(it)
# Добавили 1 категорию к статье № 2
>>> ar2.category.add(economic)
# Комментарий № 1 от пользователя (u3 — НЕ автора), под статьей о ForeignKey.on_delete (статья № 1).
>>> c1 = Comment.objects.create(user=u3, post=ar1, text="Хочется попробовать RESTRICT, но страшно 😰")
# Комментарий № 2 от от автора № 2 под новостью про первый канал (новость № 1)
>>> c2 = Comment.objects.create(user=u2, post=n1, text="😇 Первый канал лудший!")
# Комментарий № 3 от от автора № 2 под новостью из Китая (новость № 2)
>>> c3 = Comment.objects.create(user=u2, post=n2, text="Ни капли сочувствия! Звери 🥺")
# Комментарий № 4 от от автора № 1 под статьей о ставке ЦБ (статья № 2)
>>> c4 = Comment.objects.create(user=u1, post=ar2, text="💸Люблю все броши Эльвиры Сахипзадовны")

# Шесть лайков к новости № 1
>>> n1.like()
>>> n1.like()
>>> n1.like()
>>> n1.like()
>>> n1.like()
>>> n1.like()

# Два лайка к комментарию к новости № 1
>>> c2.like()
>>> c2.like()
# Лайк к статье № 2
>>> ar2.like()
# Три дизлайка к статье № 2
>>> ar2.dislike()
>>> ar2.dislike()
>>> ar2.dislike()
# Лайк к статье № 1
>>> ar1.like()
# Дизлайк к коментарию к статье № 1
>>> c1.dislike()

# Вытащили авторов через get после выхода из shell
# (много чего еще вытаскивали, зафиксировали, чтобы не забыть вытащить всё невытащенное)
>>> a1 = Author.objects.get(pk=1)
>>> a2 = Author.objects.get(pk=2)

# Обновляем рейтинг автора 1 (a1=u1=Alex: rating 27)
>>> a1.update_rating()
# Обновляем рейтинг автора 2 (a2=u2=Ivan: rating -6)
>>> a2.update_rating()

# Выводим username и рейтинг ТОП-1 автора.
# Поздравляем нашего счастливчика:  {'user__username': 'Alex', 'rating': 27}
>>> Author.objects.order_by("-rating").values("user__username", "rating")[0]

# Выбираем победителя в номинации лучшая новость/статья.
# Определяем лучшую публикацию.
>>> best_post = Post.objects.order_by("-rating").first()

# Показываем превью победителя в номинации лучшая новость/статья... Ну, кто бы сомневался:
# 'Первый канал берет новые вершины: рассказ единоросски Бутиной об очередном коварстве Америки сопровождает танцующий актер в ...'
>>> best_post.preview()

# Достаем из конверта прочую информацию о победителе:
# {'post_time': datetime.datetime(2023, 10, 30, 12, 3, 13, 528931),
# 'author__user__username': 'Alex',
# 'rating': 6,
# 'heading': 'Первый канал берет новые вершины'}
>>> Post.objects.order_by("-rating").values("post_time", "author__user__username", "rating", "heading")[0]

# Озвучиваем восторженные комментарии поклонников (дата, пользователь, рейтинг, текст) к лучшей статье.
# <QuerySet [{'comment_time': datetime.datetime(2023, 10, 30, 12, 38, 58, 98788),
# 'user__username': 'Alex',
# 'rating': 2,
# 'text': '😇 Первый канал лудший!'}]>
Comment.objects.filter(post=best_post).values("comment_time", "user__username", "rating", "text")

