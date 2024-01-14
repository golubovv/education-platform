from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User, History, Answers, QuestionsAnswers, ChoicesAnwers

# class UserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'surname', 'email', 'phone_number', 'username')
#     list_display_links = ('id', 'name', 'surname', 'username')
#     search_fields = ('id', 'name', 'surname', 'email', 'phone_number', 'username')


class HistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'user', 'lesson')
    list_display_links = ('id', 'date', 'user', 'lesson')
    search_fields = ('id', 'date', 'user', 'lesson')


class AnswersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'test_id', 'is_done', 'is_check','is_start', 'result', 'score')
    list_display_links = ('id', 'user_id', 'test_id')
    search_fields = ('id', 'user_id', 'test_id')


class QuestionsAnswersAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_answer', 'id_quest', 'is_check', 'result')
    list_display_links = ('id', 'id_answer', 'id_quest')
    search_fields = ('id', 'id_answer', 'id_quest')


class ChoicesAnwersAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_quest_answer', 'choice_answer', 'is_check', 'result')
    list_display_links = ('id', 'id_quest_answer', 'choice_answer',)
    search_fields = ('id', 'id_quest_answer', 'choice_answer',)


admin.site.register(User, UserAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(Answers, AnswersAdmin)
admin.site.register(QuestionsAnswers, QuestionsAnswersAdmin)
admin.site.register(ChoicesAnwers, ChoicesAnwersAdmin)
