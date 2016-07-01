# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-20 16:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Название аудитории')),
                ('equipment', models.BooleanField(default=False, verbose_name='Оснащенность')),
                ('seats', models.IntegerField(default=0, verbose_name='Вместимость')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=2, verbose_name='Номер курса')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Номер группы')),
                ('title', models.CharField(max_length=30, verbose_name='Название группы')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Course', verbose_name='Курс')),
            ],
        ),
        migrations.CreateModel(
            name='LearningPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=15, verbose_name='День недели')),
                ('pair', models.IntegerField(verbose_name='Пара')),
                ('alter', models.IntegerField(default=0, verbose_name='Неделя(+/-)')),
                ('audience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Audience', verbose_name='Аудитория')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Course', verbose_name='Курс')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Group', verbose_name='Группа')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('degree', models.CharField(max_length=50)),
                ('post', models.CharField(max_length=50)),
                ('faculty', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/teachers')),
            ],
        ),
        migrations.AddField(
            model_name='learningplan',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Subject', verbose_name='Дисциплина'),
        ),
        migrations.AddField(
            model_name='learningplan',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Teacher', verbose_name='Преподаватель'),
        ),
    ]
