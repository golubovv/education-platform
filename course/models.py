from django.db import models

from user.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField() #max_length
    overall_rating = models.PositiveIntegerField()
    author = models.ForeignKey(User,
                               on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True)
                                 # Или models.SET_DEFAULT категорию "без категории"
    #image = models.ImageField() #upload_to

class Chapter(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField() #max_length
    order = models.PositiveSmallIntegerField()
    course = models.ForeignKey(Course,
                               on_delete=models.SET_NULL,
                               null=True)

class Review(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE)
