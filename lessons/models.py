from django.db import models
from django.contrib.auth import get_user_model


# ********************   Модель лекции   ************************** #
class Lesson(models.Model):
    ''' В модели храняться отдельные уроки '''
    """ ВАЖНО !!!  В поле <<video>> настроить функцию upload_to !!!  """
    ''' ВАЖНО !!! Добавлено поле наличие теста и поле с id-теста, 
        придумать механизмы проверяющие данные или изменить концепции вьюхи'''

    name = models.CharField(max_length=100,
                            verbose_name='Название урока')
    video = models.FileField(verbose_name='Видео', null=True, blank=True)    # upload_to
    description = models.TextField(max_length=2000,
                                   verbose_name='Описание')
    date_create = models.DateTimeField(auto_now_add=True,
                                       verbose_name='Дата создания')
    date_publication = models.DateTimeField(verbose_name='Дата публикации',  # Реализовать логику заполнения
                                            null=True, blank=True)
    status = models.BooleanField(       # Статус, публикуется или нет, пока непонятно кто этим статусом управляет
        verbose_name='Публикация',
        default=False)
    author = models.ForeignKey(get_user_model(),
                               on_delete=models.DO_NOTHING,
                               verbose_name='Автор')
    chapter = models.ForeignKey('courses.Chapter',
                                on_delete=models.SET_NULL,
                                null=True, blank=True,
                                verbose_name='Глава')
    category = models.ForeignKey('courses.Category',
                                 on_delete=models.SET_NULL,
                                 null=True, blank=True,
                                 verbose_name='Категория')
    likes_amount = models.DecimalField(max_digits=5,
                                       decimal_places=2,
                                       verbose_name='Количество лайков', default=0)
    is_practice = models.BooleanField(default=False, verbose_name='Наличие упражнения')
    practice_nom = models.IntegerField(null=True, blank=True, verbose_name='Номер теста')

    class Meta:
        verbose_name = 'Лекция'
        verbose_name_plural = 'Лекции'

    def __str__(self):
        return f'{self.name} ({self.author})'
# ********************************************************************** #


# *****************   Модель комментарии к урокам  ********************* #
class Comment(models.Model):
    '''В модели храняться комментарии к урокам (+ответы на коментарии)
    Возможно нужно будет добавить небольшой функционал вставки <<цитаты>>, ссылок и пр. '''

    text = models.TextField(max_length=2000,
                            verbose_name='Текст')
    date = models.DateTimeField(auto_now_add=True,
                                verbose_name='Дата публикации')
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    lesson = models.ForeignKey('lessons.Lesson',
                               on_delete=models.CASCADE,
                               verbose_name='Урок')
    answer = models.ForeignKey('lessons.Comment',
                               on_delete=models.CASCADE,
                               null=True, blank=True,
                               verbose_name='Ответ на отзыв')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f"{self.lesson} {self.date} {self.user}"
# ********************************************************************** #


# ********************   Модель упражнений   *************************** #
class TestsPractice(models.Model):
    ''' Модель для упражнения, упражнения могут быть трёх видов
    1) Тесты (проверяет вьюха)
    2) Вопрос с полем для ввода ответа (проверяет вьюха, опционально + человек)
    3) Задача по программированию, с полем ввода кода (проверяет вьюха + опц. человек) '''

    name = models.CharField(max_length=150,
                            verbose_name='Название упражнения')
    description = models.TextField(max_length=2000,
                                   verbose_name='Описание')
    lesson = models.ForeignKey('lessons.Lesson',
                               on_delete=models.CASCADE,
                               verbose_name='Урок')
    #type_test = models.CharField(max_length=150, verbose_name='Тип теста')

    class Meta:
        verbose_name = 'Практика (тест)'
        verbose_name_plural = 'Практика (тесты)'
# ********************************************************************** #


# ********************   Модель вопросы   ****************************** #
class Questions(models.Model):
    ''' Модель для вопросов
    Поле <<тип вопроса>> подразумивает три вида ответа на вопрос
    1) Переключатель-радио (Один ответ из нескольких вариантов)
    2) Чекбокс (Несколько ответов, из нескольких вариантов)
    3) Словосочитание(В поле для ввода вписывается фраза или слово или цифры и т.д.) '''

    description_ques = models.TextField(max_length=2000,
                                        verbose_name='Вопрос')
    test_id = models.ForeignKey('lessons.TestsPractice',
                                on_delete=models.CASCADE,
                                verbose_name='Тест')
    num_question = models.IntegerField(verbose_name='Номер вопроса', default=0)
    type_question = models.CharField(max_length=150,
                                     verbose_name='Тип вопроса')

    class Meta:
        verbose_name = 'Вопросы к тестам'
        verbose_name_plural = 'Вопрос'
# ********************************************************************** #


# ***************   Модель варианты ответов к вопросам ***************** #
class Choices(models.Model):
    ''' Модель для вариантов ответа
    изначально подразумивалось для вопросов типа тесты,
    поэтому возможно придеться доработать модель для вопросов без вариантов ответа '''

    choice_answer = models.TextField(max_length=2000,
                                     verbose_name='Вариант ответа')
    is_correct = models.BooleanField(default=False, verbose_name='Верно Да/Нет')
    Questions = models.ForeignKey('lessons.Questions',
                                  on_delete=models.CASCADE,
                                  verbose_name='Вопрос')

    class Meta:
        verbose_name = 'Варианты к вопросам'
        verbose_name_plural = 'Вариант ответа'
# ********************************************************************** #

