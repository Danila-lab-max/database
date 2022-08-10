from .models import Teacher, Student, Texts
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, EmailField, NumberInput, EmailInput


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['last_name_teacher', 'first_name_teacher', 'school_teacher', 'email_teacher', 'password_teacher']

        widgets = {
            'last_name_teacher': TextInput(attrs={
                'class': 'form_control'
            }),
            'first_name_teacher': TextInput(attrs={
                'class': 'form_control'
            }),
            'school_teacher': NumberInput(attrs={
                'class': 'form_control'
            }),
            'email_teacher': EmailInput(
            ),
            'password_teacher': TextInput(attrs={
                'class': 'form_control'
            })
        }


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['last_name_student', 'first_name_student', 'email_student', 'password_student']

        widgets = {
            'last_name_student': TextInput(attrs={
                'class': 'form_control'
            }),
            'first_name_student': TextInput(attrs={
                'class': 'form_control'
            }),
            'email_student': EmailInput(
            ),
            'password_student': TextInput(attrs={
                'class': 'form_control'
            })
        }


class TextForm(ModelForm):
    class Meta:
        model = Texts
        fields = ['title', 'text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form_control'
            }),
            'text': Textarea(attrs={
                'class': 'form_control'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form_control'
            }
            )
        }
