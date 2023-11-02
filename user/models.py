from django.db import models


# Модель Пользователи (User)
class User(models.Model):
    name = models.CharField(max_length=50)              # Название
    surname = models.CharField(max_length=50)           # Фамилия
    email = models.EmailField(unique=True)              # Почта
    phone_number = models.CharField(unique=True, max_length=20)  # Поле и длина под вопросом
    photo = models.ImageField()                         # Фото пользоваьтеля upload_to
    subs = models.ManyToManyField('user.User')          # Подписки
    likes = models.ManyToManyField('lesson.Lesson',     # Лайки урокам
                                   related_name='liked_lessons')
    favorites = models.ManyToManyField('lesson.Lesson', # Избраное уроки
                                       related_name='favorite_lessons')
    nikname = models.SlugField()                        # Уникальное имя пользователя


# Модель История (History)
class History(models.Model):
    date = models.DateTimeField(auto_now_add=True)      # Дата
    user = models.ForeignKey(User,                      # ID_ пользователя
                             on_delete=models.CASCADE)
    lesson = models.ForeignKey('lesson.Lesson',         # ID_ Урока
                               on_delete=models.CASCADE)
    # Одна запись - один урок в истории, легко сортировать по дате просмотра
    # ----------------- Или ----------------------
    # Одна запись - все уроки, не знаю как будет проходить сортировка по дате
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # lessons = models.ManyToManyField(Lesson)
