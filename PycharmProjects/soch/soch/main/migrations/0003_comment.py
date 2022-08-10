# Generated by Django 3.2.13 on 2022-05-25 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220526_0028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(default='', max_length=500, verbose_name='Comment')),
                ('checking_text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.texts')),
            ],
        ),
    ]
