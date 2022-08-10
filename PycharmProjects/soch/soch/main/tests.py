from django.test import TestCase
from .models import Student, Teacher, Texts
from datetime import datetime


class ModelsTestCase(TestCase):
    def test(self):
        s1 = Student(first_name='Danila', last_name='Ivanov', email='dan@gmail.com', password='222')
        s1.save()

        t1 = Teacher(first_name='Danila', last_name='Ivanov', email='dan@gmail.com', password='222',
                     school=333)
        t1.save()
        text1 = Texts(title='Война и мир', text='«Предмет истории есть жизнь народов и человечества»,'
                                                '– так начинает Л.Н.Толстой вторую часть '
                                                'эпилога романа-эпопеи «Война и мир». ',
                      date=datetime.now(),
                      id_creater=s1, id_checking=t1)
        text1.save()
        print(text1.id_creater)
