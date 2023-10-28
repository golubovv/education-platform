from django.db import models

# Модель Категории (Category)
class Category(models.Model):
    name = models.CharField(max_length=100) # Наименование главы
    slug = models.SlugField()               # Порядок главы в курсе

# Модель Курсы (Course)
# Почему category null=True
class Course(models.Model):
    name = models.CharField(max_length=100)                                 # Название
    description = models.TextField()                                        # Описание, max_length
    overall_rating = models.DecimalField(max_digits=5, decimal_places=2)    # Рейтинг, У нас рейтинг складывается из оценок.
    author = models.ForeignKey('user.User',                                 # ID_ Пользователь, связь с пользователем. он же автор
                               on_delete=models.DO_NOTHING)
    category = models.ForeignKey('course.Category',                         # Категория,
                                 on_delete=models.SET_NULL,
                                 null=True)

# Модель Глава(Chapter)
class Chapter(models.Model):
    name = models.CharField(max_length=100)             # Название
    description = models.TextField()                    # Описание, max_length
    order = models.PositiveSmallIntegerField()          # Нужна ли глава,
    course = models.ForeignKey('course.Course',         # ID_ Курса
                               on_delete=models.SET_NULL,
                               null=True)

#  Модель Отзывы на курс (Review)
# Общий вопрос по отзывам, как ограничить количество оценок на урок, курс дляодного пользователя
class Review(models.Model):
    user = models.ForeignKey('user.User',               # ID_ пользователя
                             on_delete=models.CASCADE)
    course = models.ForeignKey('course.Course',         # ID_ Курса
                               on_delete=models.CASCADE)
    text = models.TextField(max_length=2000)                        # Текст, комментарий
    value = models.PositiveSmallIntegerField()          # Оценка
    date = models.DateTimeField(auto_now_add=True)      # Дата отзыва

