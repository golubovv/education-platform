from django.db import models


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    video = models.FileField() #upload_to
    description = models.TextField() #max_length
    date_create = models.DateTimeField(auto_now_add=True)
    date_publication = models.DateTimeField() #Реализовать логику заполнения
    status = models.BooleanField()
    author = models.ForeignKey('user.User',
                               on_delete=models.DO_NOTHING)
    chapter = models.ForeignKey('course.Chapter',
                                on_delete=models.SET_NULL,
                                null=True)
    #likes = models.PositiveIntegerField()

class Comment(models.Model):
    text = models.TextField(max_length=2000)
    date = models.DateTimeField(auto_now_add=True)
    User = models.ForeignKey('user.User',
                             on_delete=models.CASCADE)
    lesson = models.ForeignKey('lesson.Lesson',
                               on_delete=models.CASCADE)
    answer = models.ForeignKey('lesson.Comment',
                               on_delete=models.CASCADE)
