from django.db import models

# Добавил коментарий
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

def get_path_save1(instance,filename):
    str1 = '{0}\\{1}'.format(instance.author, filename)     # Только функцию нужно доделать чтобы она не пыталась создать
    return str1                                             # папку с таким же именем

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField() #max_length
    overall_rating = models.PositiveIntegerField()
    author = models.ForeignKey('user.User',
                               on_delete=models.DO_NOTHING)
    category = models.ForeignKey('course.Category',
                                 on_delete=models.SET_NULL,
                                 null=True)
    video = models.FileField(upload_to=get_path_save1, verbose_name='Файл видео урока')
                                 # Или models.SET_DEFAULT категорию "без категории"
    #image = models.ImageField() #upload_to

class Chapter(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField() #max_length
    order = models.PositiveSmallIntegerField()
    course = models.ForeignKey('course.Course',
                               on_delete=models.SET_NULL,
                               null=True)

class Review(models.Model):
    user = models.ForeignKey('user.User',
                             on_delete=models.CASCADE)
    course = models.ForeignKey('course.Course',
                               on_delete=models.CASCADE)
