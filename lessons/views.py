from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, View
from .models import Lesson, TestsPractice, Questions, Choices
from .forms import CreateLesson, CreatePractice, CreateChoices2, CreateQuestions
from django.urls import reverse_lazy
from courses.models import Course, Chapter
from django.shortcuts import render


# Класс-контроллер для вывода списка всех "Курсов"
class LessonsList(ListView):
    model = Lesson
    template_name = 'lessons/lessons_list.html'
    context_object_name = 'lessons'


# Класс-контроллер для создания уроков, LoginRequiredMixin - ограничение доступа к странице
class AddLesson(LoginRequiredMixin, CreateView):
    form_class = CreateLesson
    template_name = 'lessons/createlesson.html'
    pk_url_kwarg = 'course_id4'
    context_object_name = 'lessons'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chapter'] = Chapter.objects.filter(pk=self.kwargs['chapter_id'])
        # Вприцепи можно было обойтись и без context['chapter'],
        # т.к модель chapter и course связаны, то
        # например, чтобы в шаблоне обратиться pk-главы можно использовать course.chapter.pk
        context['course'] = Course.objects.filter(pk=self.kwargs['course_id4'])
        return context

    def get_success_url(self):
        return reverse_lazy('edit_course', args=[self.kwargs['course_id4']])

    # Переопределение метода проверки формы перед сохранением, для присвоения id-пользователя к полю id-автор
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author_id = self.request.user.pk
        obj.course_id = self.kwargs['course_id4']
        obj.chapter_id = self.kwargs['chapter_id']
        obj.save()
        return super().form_valid(form)


# Контроллер для редактирования Уроков(лекций)
class EditLessons(View):
    # Переопределяю метод get, передавая параметр id-урока
    def get(self, request, lesson_id):
        Lesson1 = Lesson.objects.get(pk=lesson_id)      # Нахожу "объект" урока
        Lesson_form = CreateLesson(instance=Lesson1)    # Заполняю форму данными из "объекта" урока
        # Теперь рендерю шаблон с данными в форме
        return render(request, 'lessons\editlesson.html', context={'Lesson_form': Lesson_form, 'lesson': Lesson1})

    # Тут переопределяем медод post
    # делаеется тоже самое, только добавлено в форму данные из post и
    # добавленно условие сохранения формы при валидации
    def post(self, request, lesson_id):
        Lesson1 = Lesson.objects.get(pk=lesson_id)
        Lesson_form = CreateLesson(request.POST, instance=Lesson1)

        if Lesson_form.is_valid():
            Lesson1.save()
        return render(request, 'lessons\editlesson.html', context={'Lesson_form': Lesson_form, 'lesson': Lesson1})


# Класс-контроллер для создания упражнения(тест) к уроку
class AddTestsPractice(CreateView):
    form_class = CreatePractice
    template_name = 'lessons/createpractice.html'
    pk_url_kwarg = 'lesson_id'

    # Переопределение метода для добавления данных,
    # тех данных которые должны заполниться "автоматически"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Ниже наверно нужно было использовать get вместо
        # filter Lesson.objects.get(pk=self.kwargs['lesson_id']),
        # поэтому в шаблоне обращение lesson.0.name, нулевой объект
        context['lesson'] = Lesson.objects.filter(pk=self.kwargs['lesson_id'])
        return context

    # Переопределяем метод прохождения валидации формы
    # Если форма валидна(правильная) то вызовется этот медод
    def form_valid(self, form):
        obj = form.save(commit=False)                       # Остановка валидации
        obj.lesson_id = self.kwargs['lesson_id']            # Привязка "упражнения" к уроку по lesson_id
        obj.save()                                          # Сохраниение
        # Следующие три действия нужны чтобы поставить "флаг" наличия упражнения у урока
        obj2 = Lesson.objects.filter(pk=self.kwargs['lesson_id'])   # выборка урока
        obj = obj2[0]                                       # Вспомогательное действие
        obj.is_practice = True                              # Установка флага
        # Неуверен что остальное нужно
        # obj2 = TestsPractice.objects.filter(lesson__pk=obj.pk)
        # obj.practice_nom = obj2[0].pk
        obj.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home')


# Класс-контроллер для просмотра и редактирования упражнения(тест) к уроку
class EditTestsPractice(View):

    def get(self, request, lesson_id):
        Lesson1 = Lesson.objects.get(pk=lesson_id)
        practice = TestsPractice.objects.get(lesson__pk=lesson_id)
        question = Questions.objects.filter(test_id=practice.pk)
        questions = {}
        k = 0
        for i in question.order_by('num_question'):
            list_a = []
            num_question = f'question_{k}'
            list_a.append(i)
            list_a.append(Choices.objects.filter(Questions__pk=i.pk))
            questions[num_question] = list_a
            k = 1 + k
        return render(request, 'lessons/edit_practice_ext.html', context={'practice': practice, 'questions': questions, 'lesson': Lesson1})


# Класс-контроллер для создания вопроса к упражнению(тест)
class CreateQustions(CreateView):
    form_class = CreateQuestions
    template_name = 'lessons/createquiston.html'
    pk_url_kwarg = 'test_id'
    context_object_name = 'Questions'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['practice'] = TestsPractice.objects.get(pk=self.kwargs['test_id'])
        context['lesson'] = Lesson.objects.get(pk=context['practice'].lesson.pk)
        context['Chapter1'] = Chapter.objects.get(pk=context['lesson'].chapter.pk)
        context['courses'] = Course.objects.get(pk=context['Chapter1'].course.pk)
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.test_id = TestsPractice.objects.get(pk=self.kwargs['test_id'])
        obj.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home')


class EditQuestion(View):

    def get(self, request, quistion_id):
        Quistion = Questions.objects.get(pk=quistion_id)
        Quistion_form = CreateQuestions(instance=Quistion)
        return render(request, 'lessons\editquistion.html', context={'Quistion_form': Quistion_form, 'Quistion': Quistion})

    def post(self, request, quistion_id):
        Quistion = Questions.objects.get(pk=quistion_id)
        Quistion_form = CreateQuestions(request.POST, instance=Quistion)

        if Quistion_form.is_valid():
            Quistion_form.save()
        return render(request, 'lessons\editquistion.html', context={'Quistion_form': Quistion_form, 'Quistion': Quistion})


# Класс-контроллер для изменения упражнений(тест)
class EditPractice(View):

    def get(self, request, test_id):
        test = TestsPractice.objects.get(pk=test_id)
        test_form = CreatePractice(instance=test)
        return render(request, 'lessons\editpractice.html', context={'test_form': test_form, 'test_id': test_id,
                                                                     'test': test})

    def post(self,request, test_id):
        test = TestsPractice.objects.get(pk=test_id)
        test_form = CreatePractice(request.POST, instance=test)

        if test_form.is_valid():
            test.save()
        return render(request, 'lessons\editpractice.html', context={'test_form': test_form, 'test_id': test_id,
                                                                     'test': test})

# Класс-контроллер для создания варианта ответа
class CreateChoices(CreateView):
    form_class = CreateChoices2
    template_name = 'lessons/createchoices.html'
    pk_url_kwarg = 'question_id'
    context_object_name = 'choice'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question'] = Questions.objects.get(pk=self.kwargs['question_id'])
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.Questions = Questions.objects.get(pk=self.kwargs['question_id'])
        obj.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home')


# Класс-контроллер для изменения варианта ответа
class EditChoices(View):

    def get(self, request, choic_id):
        Choic = Choices.objects.get(pk=choic_id)
        Choic_form = CreateChoices2(instance=Choic)
        return render(request, 'lessons\editchoic.html', context={'Choic_form': Choic_form, 'Choic': Choic})

    def post(self, request, choic_id):
        Choic = Choices.objects.get(pk=choic_id)
        Choic_form = CreateChoices2(request.POST, instance=Choic)

        if Choic_form.is_valid():
            Choic_form.save()
        return render(request, 'lessons\editchoic.html', context={'Choic_form': Choic_form, 'Choic': Choic})