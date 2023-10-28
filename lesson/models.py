from django.db import models

from user.models import User
from course.models import Chapter

class Lesson(models.Model):
    name = models.CharField(max_length=100)
    video = models.FileField() #upload_to
    description = models.TextField() #max_length
    date_create = models.DateTimeField(auto_now_add=True)
    date_publication = models.DateTimeField() #Реализовать логику заполнения
    status = models.BooleanField()
    author = models.ForeignKey(User,
                               on_delete=models.DO_NOTHING())
    chapter = models.ForeignKey(Chapter,
                                on_delete=models.SET_NULL,
                                null=True)
    #likes = models.PositiveIntegerField()

class Comment(models.Model):
    text = models.TextField(max_length=2000)
    date = models.DateTimeField(auto_now_add=True)
    User = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson,
                               on_delete=models.CASCADE)
    answer = models.ForeignKey(Comment,
                               on_delete=models.CASCADE)
