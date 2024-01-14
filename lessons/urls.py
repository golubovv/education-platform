from django.urls import path

from .views import LessonsList, AddLesson, AddTestsPractice, EditTestsPractice, CreateQustions, EditPractice,\
    EditLessons, EditQuestion, CreateChoices, EditChoices

url_patterns = [
    path('lessons_list', LessonsList.as_view(), name='lessons_list'),
    path('create-lesson/<int:course_id4>/<int:chapter_id>', AddLesson.as_view(), name='create_lesson'),
    path('create-practice/<int:lesson_id>', AddTestsPractice.as_view(), name='create_practice'),
    path('view-practice/<int:lesson_id>', EditTestsPractice.as_view(), name='view_practice'),
    path('create-quistion/<int:test_id>', CreateQustions.as_view(), name='create_quistion'),
    path('edit-practice/<int:test_id>', EditPractice.as_view(), name='edit_practice'),
    path('edit-lesson/<int:lesson_id>', EditLessons.as_view(), name='edit_lesson'),
    path('edit-quistion/<int:quistion_id>', EditQuestion.as_view(), name='edit_quistion'),
    path('create-choices/<int:question_id>', CreateChoices.as_view(), name='create_choices'),
    path('edit-choices/<int:choic_id>', EditChoices.as_view(), name='edit_choic'),
]
