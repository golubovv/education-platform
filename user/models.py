from django.db import models


# Модель Пользователи (User)
class User(models.Model):
    name = models.CharField(max_length=50,              # Название
                            verbose_name='Имя')
    surname = models.CharField(max_length=50,           # Фамилия
                               verbose_name='Фамилия')
    email = models.EmailField(unique=True,              # Почта
                              verbose_name='почта')
    phone_number = models.CharField(unique=True,        # Поле и длина под вопросом
                                    max_length=20,
                                    verbose_name='Номер тел.')
    photo = models.ImageField(verbose_name='Фото',      # Фото пользоваьтеля upload_to
                              blank=True, null=True)
    subs = models.ManyToManyField('user.User',          # Подписки
                                  verbose_name='Подписки',
                                  blank=True,null=True)
    likes = models.ManyToManyField('lesson.Lesson',             # Лайки урокам
                                   related_name='liked_lessons',
                                   verbose_name='Лайки',
                                   blank=True, null=True)
    favorites = models.ManyToManyField('lesson.Lesson',         # Избраное уроки
                                       related_name='favorite_lessons',
                                       verbose_name='Избранное',
                                       blank=True, null=True)
    nikname = models.SlugField(verbose_name='НикНейм')          # Уникальное имя пользователя

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        name_2name = str(self.pk) + ' ' + str(self.surname) + ' ' + str(self.name)
        return name_2name


# Модель История (History)
class History(models.Model):
    date = models.DateTimeField(auto_now_add=True,      # Дата
                                verbose_name='Дата')
    user = models.ForeignKey(User,                      # ID_ пользователя
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    lesson = models.ForeignKey('lesson.Lesson',         # ID_ Урока
                               on_delete=models.CASCADE,
                               verbose_name='Лекция')
    # Одна запись - один урок в истории, легко сортировать по дате просмотра
    # ----------------- Или ----------------------
    # Одна запись - все уроки, не знаю как будет проходить сортировка по дате
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # lessons = models.ManyToManyField(Lesson)

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'История просмотров'

    def __str__(self):
        lesson_user_date = self.lesson + ' ' + self.user + ' ' + self.date
        return lesson_user_date
