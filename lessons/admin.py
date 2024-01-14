from django.contrib import admin
from .models import Lesson, Comment, TestsPractice, Questions, Choices
# Register your models here.


class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'chapter', 'category', 'author')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'category', 'author')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'user', 'lesson')
    list_display_links = ('id', 'date', 'user', 'lesson')
    search_fields = ('id', 'date', 'user', 'lesson')


class TestsPracticeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lesson')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'lesson')


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'test_id', 'num_question', 'description_ques')
    list_display_links = ('id', 'test_id', 'num_question')
    search_fields = ('id', 'test_id', 'num_question')


class ChoicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'Questions', 'choice_answer', 'is_correct')
    list_display_links = ('id', 'Questions', 'choice_answer')
    search_fields = ('id', 'Questions', 'choice_answer')


admin.site.register(Lesson, LessonAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(TestsPractice, TestsPracticeAdmin)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Choices, ChoicesAdmin)
