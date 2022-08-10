from django.shortcuts import render, redirect
from .models import Student, Texts, Teacher, Comment
from .forms import TeacherForm, StudentForm, TextForm
from datetime import datetime
from django.views.generic import DetailView


def main(request):
    request.session['user'] = ''
    request.session['user_email'] = ''
    request.session['user_name'] = ''
    request.session['email_student'] = ''
    request.session['email_teacher'] = ''
    return redirect('home')


# Create your views here.
def home(request):
    texts = Texts.objects.order_by('-date')
    return render(request, 'main/index.html',
                  {'texts': texts, 'log': request.session['user'], 'name': request.session['user_name']})


class SochDetailView(DetailView):
    model = Texts
    template_name = 'main/detail_view.html'
    context_object_name = 'text'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.request.session['user_name']
        context['log'] = self.request.session['user']
        try:
            context['comment'] = Comment.objects.get(checking_text=kwargs['object'])
        except:
            pass
        return context


def regist_teacher(request):
    error = ''
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        form.save()

        request.session['user'] = 'teacher'
        request.session['user_email'] = request.POST['email_teacher']
        request.session['user_name'] = request.POST['first_name_teacher']
        request.session['email_teacher'] = form.cleaned_data['email_teacher']
        return redirect('home')
    form = TeacherForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/regist_teacher.html', data)


def regist_student(request):
    error = ''
    if request.method == 'POST':
        form = StudentForm(request.POST)
        form.save()

        request.session['user'] = 'student'
        request.session['user_email'] = request.POST['email_student']
        request.session['user_name'] = request.POST['first_name_student']
        request.session['email_student'] = form.cleaned_data['email_student']
        return redirect('home')
    form = StudentForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/regist_student.html', data)


def entrance(request):
    error = ''
    if request.method == 'POST':
        try:
            user_s = Student.objects.get(email_student=request.POST['email'], password_student=request.POST['password'])
            request.session['user'] = 'student'
            request.session['user_email'] = user_s.email_student
            request.session['user_name'] = user_s.first_name_student
            request.session['email_student'] = user_s.email_student
            return redirect('home')
        except:
            try:
                user_t = Teacher.objects.get(email_teacher=request.POST['email'],
                                             password_teacher=request.POST['password'])
                request.session['user'] = 'teacher'
                request.session['user_email'] = user_t.email_teacher
                request.session['user_name'] = user_t.first_name_teacher
                request.session['email_teacher'] = user_t.email_teacher
                return redirect('home')
            except:
                error = 'Not found this user'
    return render(request, 'main/log.html', {'error': error})


def create(request):
    s = Student.objects.get(email_student=request.session['email_student'])
    error = ''
    if request.method == 'POST':
        text = Texts(title=request.POST['title'], text=request.POST['text'],
                     date=request.POST['date'],
                     id_creater=s)
        text.save()

        return redirect('home')
    form = TextForm
    data = {
        'form': form,
        'log': request.session['user'],
        'name': request.session['user_name']
    }
    return render(request, 'main/create.html', data)


def create_comment(request):
    t = Texts.objects.get(id=request.POST['text'])
    c = Comment(comment=request.POST['comment'], checking_text=t)
    c.save()
    Texts.objects.filter(id=request.POST['text']).update(
        id_checking=Teacher.objects.get(email_teacher=request.session['email_teacher']))
    return redirect('home')
