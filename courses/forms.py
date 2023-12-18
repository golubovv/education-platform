#from django.forms import ModelForm, TextInput, Textarea, Select, NumberInput
from django import forms
from .models import Course, Chapter


# Форма создания курса
class CreateCourse(forms.ModelForm):

    class Meta:
        model = Course
        fields = ('name', 'description', 'category', 'price')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', "rows": '4'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'})
        }


# Форма создания главы
class CreateChapter(forms.ModelForm):

    class Meta:
        model = Chapter
        fields = ('name', 'order', 'description')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', "rows": '4'}),
        }


class SubToCourseForm(forms.Form):
    #fields = ('post', )
    pass
