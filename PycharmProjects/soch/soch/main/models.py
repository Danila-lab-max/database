from django.db import models


class Student(models.Model):
    first_name_student = models.CharField('Имя', max_length=30)
    last_name_student = models.CharField('Фамилия', max_length=30)
    email_student = models.EmailField('Email')
    password_student = models.CharField('Password', max_length=30)

    def __str__(self):
        return f'{self.first_name_student} {self.last_name_student}'


class Teacher(models.Model):
    first_name_teacher = models.CharField('Имя', max_length=30)
    last_name_teacher = models.CharField('Фамилия', max_length=30)
    email_teacher = models.EmailField('Email')
    school_teacher = models.IntegerField('Номер школы')
    password_teacher = models.CharField('Password', max_length=30)

    def __str__(self):
        return f'{self.first_name_teacher} {self.last_name_teacher}'


class Texts(models.Model):
    title = models.CharField('Тема', max_length=50, default='')
    text = models.CharField('Текст', max_length=500, default='')
    date = models.DateTimeField('Дата')
    id_creater = models.ForeignKey(Student, on_delete=models.CASCADE)
    id_checking = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    checking_text = models.ForeignKey(Texts, on_delete=models.CASCADE)
    comment = models.CharField('Комментарий', max_length=500, default='')

    def __str__(self):
        return self.comment
