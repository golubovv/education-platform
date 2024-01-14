from django.forms import ModelForm, TextInput, Textarea, Select, NumberInput, CheckboxInput, Form
from .models import Lesson, TestsPractice, Questions, Choices
from django import forms

# Форма создания урока
class CreateLesson(ModelForm):
    ''' Форма создания уроков оооочень сырая
        в дальнейшем это должно быть более функциональная форма,
        более чем просто два поля... '''

    class Meta:
        model = Lesson
        fields = ('name', 'description')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', "rows": '4'}),
        }


# Форма создания Упражнения после урока
class CreatePractice(ModelForm):
    ''' Форма создания упражнений тоже оооочень сырая '''

    class Meta:
        model = TestsPractice
        fields = ('name', 'description')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', "rows": '4'})
        }


# Список для выбора тип вопроса, <<тест>>, <<вопрос-ответ>>, <<задача скодом>>.
type_questions = [
    ('TEST', 'Тест'),
    ('Question', 'Вопрос-ОТВЕТ'),
    ('Code', 'Задача с кодом'),
]
# использовать так widget=forms.Select(choices=type_questions))


# Форма создания Вопроса после урока
class CreateQuestions(ModelForm):
    ''' Форма создания вопросов тоже оооочень сырая '''

    class Meta:
        model = Questions
        fields = ('description_ques', 'num_question', 'type_question')
        widgets = {
            'description_ques': Textarea(attrs={'class': 'form-control', "rows": '3'}),
            'num_question': NumberInput(attrs={'class': 'form-control'}),
            'type_question': Select(choices=type_questions, attrs={'class': 'form-control'})
        }


# Форма создания Варианта ответа на вопрос после урока
class CreateChoices2(ModelForm):
    ''' Форма создания варианта ответат на вопрос '''

    class Meta:
        model = Choices
        fields = ('choice_answer', 'is_correct')
        widgets = {
            'choice_answer': TextInput(attrs={'class': 'form-control'}),
            'is_correct': CheckboxInput(attrs={'class': 'form-control'})
        }


# Форма создания Варианта ответа к вопросу
"""class CreateQuestionsChoices(forms.Form):
    description_ques = forms.CharField(label='Вопрос(упражнение)', widget=forms.Textarea(attrs={
                                                                                                'class': 'form-control',
                                                                                                'rows': '4'}))
    num_question = forms.IntegerField(label='Номер вопроса', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    type_question = forms.ChoiceField(label='Тип вопроса', choices=type_questions)
    choice_answer = forms.CharField(label='Вариант ответа', widget=forms.Textarea(attrs={'class': 'form-control',
                                                                                         'rows': '4'}))
    is_correct = forms.BooleanField(label='Верно Да/Нет', widget=forms.CheckboxInput(attrs={'class': 'form-control'}))"""
