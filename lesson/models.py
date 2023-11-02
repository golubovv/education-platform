from django.db import models


# Модель Уроки (Lesson)
class Lesson(models.Model):
    name = models.CharField(max_length=100)                     # Название
    video = models.FileField()                                  # Файл видео, upload_to
    description = models.TextField()                            # Описание, max_length
    date_create = models.DateTimeField(auto_now_add=True)       # Дата создания
    date_publication = models.DateTimeField()                   # Дата публикации, Реализовать логику заполнения
    status = models.BooleanField()                              # Статус, публикуется или нет, пока непонятно кто этим статусом управляет
    author = models.ForeignKey('user.User',                     # ID_ Пользователь
                               on_delete=models.DO_NOTHING)
    chapter = models.ForeignKey('course.Chapter',               # ID_ Глава
                                on_delete=models.SET_NULL,
                                null=True)
    category = models.ForeignKey('course.Category',             # Категория
                                 on_delete=models.SET_NULL,
                                 null=True)
    overall_rating = models.DecimalField(max_digits=5,          # Рейтинг, У нас рейтинг складывается из оценок.
                                         decimal_places=2)


# Модель Отзывы уроков (Comment)
# Почему User с большой буквы
class Comment(models.Model):
    text = models.TextField(max_length=2000)                # Текст
    date = models.DateTimeField(auto_now_add=True)          # Дата
    User = models.ForeignKey('user.User',                   # ID_ пользователя
                             on_delete=models.CASCADE)
    lesson = models.ForeignKey('lesson.Lesson',             # ID_ Урока
                               on_delete=models.CASCADE)
    answer = models.ForeignKey('lesson.Comment',            # ID_ Отзыва2
                               on_delete=models.CASCADE,
                               null=True)


