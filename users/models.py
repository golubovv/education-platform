from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=True)
    phone_number = models.CharField(unique=True,        # Поле под вопросом
                                    max_length=20,
                                    verbose_name='Номер тел.',
                                    blank=True, null=True)
    photo = models.ImageField(verbose_name='Фото',      # upload_to
                              blank=True, null=True)
    subs = models.ManyToManyField('users.User',          # Подписки
                                  verbose_name='Подписки',
                                  blank=True)
    likes = models.ManyToManyField('lessons.Lesson',             # Лайки урокам
                                   related_name='liked_lessons',
                                   verbose_name='Лайки',
                                   blank=True)
    favorites = models.ManyToManyField('lessons.Lesson',         # Избраное уроки
                                       related_name='favorite_lessons',
                                       verbose_name='Избранное',
                                       blank=True)
    
    def get_absolute_url(self):
        return reverse('profile', kwargs={'username': self.username})

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'



class History(models.Model):
    date = models.DateTimeField(auto_now_add=True,
                                verbose_name='Дата')
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    lesson = models.ForeignKey('lessons.Lesson',
                               on_delete=models.CASCADE,
                               verbose_name='Урок')

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'История просмотров'

    def __str__(self):
        return f'{self.date} ({self.user}) ({self.lesson})'


class Answers(models.Model):
    user_id = models.ForeignKey(get_user_model(),
                                on_delete=models.CASCADE,
                                verbose_name='Пользователь')
    test_id = models.ForeignKey('lessons.TestsPractice',
                                on_delete=models.CASCADE,
                                verbose_name='Тест')
    date = models.DateTimeField(auto_now_add=True,
                                verbose_name='Дата начала')
    is_done = models.BooleanField(default=False, verbose_name='Закончен')
    is_check = models.BooleanField(default=False, verbose_name='Проверен')
    result = models.BooleanField(default=False, verbose_name='Зачтено')
    score = models.DecimalField(max_digits=5,
                                decimal_places=2,
                                verbose_name='Количество балов', default=0)

    class Meta:
        verbose_name = 'Результаты тестов'
        verbose_name_plural = 'результат теста'


class QuestionsAnswers(models.Model):
    id_answer = models.ForeignKey(
        'users.TestsPractice',
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    id_quest = models.ForeignKey(
        'lessons.Questions',
        on_delete=models.CASCADE,
        verbose_name='Вопрос'
    )
    #is_done = models.BooleanField(default=False, verbose_name='Проверено')
    is_check = models.BooleanField(default=False, verbose_name='Проверено')
    result = models.BooleanField(default=False, verbose_name='Верно')

    class Meta:
        verbose_name = 'Результаты на вопросы'
        verbose_name_plural = 'Результат вопроса'


class ChoicesAnwers(models.Model):
    choice_answer = models.CharField(max_length=150,
                                     verbose_name='Ответ пользователя')
    id_quest_answer = models.ForeignKey(
        'users.QuestionsAnswers',
        on_delete=models.CASCADE,
        verbose_name='Вопрос'
    )
    is_check = models.BooleanField(default=False, verbose_name='Проверено')
    result = models.BooleanField(default=False, verbose_name='Верно')

    class Meta:
        verbose_name = 'Варианты ответов'
        verbose_name_plural = 'Вариант ответа'

