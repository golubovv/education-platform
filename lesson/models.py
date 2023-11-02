from django.db import models


# Модель Уроки (Lesson)
class Lesson(models.Model):
    name = models.CharField(max_length=100,                     # Название
                            verbose_name='Наименование лекции')
    video = models.FileField(verbose_name='Видео')              # Файл видео, upload_to
    description = models.TextField(verbose_name='Описание')     # Описание, max_length
    date_create = models.DateTimeField(auto_now_add=True,
                                       verbose_name='Дата создания')            # Дата создания
    date_publication = models.DateTimeField(verbose_name='Дата публикации')     # Дата публикации, Реализовать логику заполнения
    status = models.BooleanField(verbose_name='Публикация')     # Статус, публикуется или нет, пока непонятно кто этим статусом управляет
    author = models.ForeignKey('user.User',                     # ID_ Пользователь
                               on_delete=models.DO_NOTHING,
                               verbose_name='Автор')
    chapter = models.ForeignKey('course.Chapter',               # ID_ Глава
                                on_delete=models.SET_NULL,
                                null=True,
                                verbose_name='Глава')
    category = models.ForeignKey('course.Category',             # Категория
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 verbose_name='Категория')
    overall_rating = models.DecimalField(max_digits=5,          # Рейтинг, У нас рейтинг складывается из оценок.
                                         decimal_places=2,
                                         verbose_name='Рейтинг')

    class Meta:
        verbose_name = 'Лекция'
        verbose_name_plural = 'Лекции'

    def __str__(self):
        name_author = self.name + ' ' + self.author
        return name_author


# Модель Отзывы уроков (Comment)
# Почему User с большой буквы
class Comment(models.Model):
    text = models.TextField(max_length=2000,                # Текст
                            verbose_name='Текст')
    date = models.DateTimeField(auto_now_add=True,          # Дата
                                verbose_name='Дата')
    User = models.ForeignKey('user.User',                   # ID_ пользователя
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    lesson = models.ForeignKey('lesson.Lesson',             # ID_ Урока
                               on_delete=models.CASCADE,
                               verbose_name='Лекция')
    answer = models.ForeignKey('lesson.Comment',            # ID_ Отзыва2
                               on_delete=models.CASCADE,
                               null=True,
                               verbose_name='Ответ на отзыв')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        lesson_date_User = self.lesson + ' ' + self.date + ' ' + self.User
        return lesson_date_User
