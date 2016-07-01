from django.db import models

# Create your models here.

class Teacher(models.Model):
	name = models.CharField(max_length=60)
	degree = models.CharField(max_length=50)
	post = models.CharField(max_length=50)
	faculty = models.CharField(max_length=50)
	phone = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	image = models.ImageField(upload_to='images/teachers')
	def __str__(self):
		return self.name

class Subject(models.Model):
	title = models.CharField(max_length=100)
	def __str__(self):
		return self.title

class Audience(models.Model):
	title = models.CharField("Название аудитории", max_length=60)
	equipment = models.BooleanField("Оснащенность", default=False)
	seats = models.IntegerField("Вместимость", default=0)
	def __str__(self):
		return '%s, %s, %s' % (self.title, self.equipment, self.seats)

class Course(models.Model):
	number = models.CharField("Номер курса", max_length=2)
	def __str__(self):
		return self.number

class Group(models.Model):
	number = models.IntegerField("Номер группы")
	title = models.CharField("Название группы", max_length=30)
	course = models.ForeignKey(Course, verbose_name="Курс")
	students = models.TextField()
	def __str__(self):
		return '%s, %s' % (self.number, self.title)

class Day(models.Model):
	titleRus = models.CharField("День недели", max_length=3)
	titleEng = models.CharField("Day of week", max_length=3)
	def __str__(self):
		return self.titleRus

class Pair(models.Model):
	time = models.CharField("Время", max_length=15)
	pair = models.IntegerField("Номер пары")
	def __str__(self):
		return self.time

class LearningPlan(models.Model):
	teacher = models.ForeignKey(Teacher, verbose_name="Преподаватель")
	subject = models.ForeignKey(Subject, verbose_name="Дисциплина")
	course = models.ForeignKey(Course, verbose_name="Курс")
	group = models.ForeignKey(Group, verbose_name="Группа")
	audience = models.ForeignKey(Audience, verbose_name="Аудитория")
	day = models.ForeignKey(Day, verbose_name="День недели")
	pair = models.ForeignKey(Pair, verbose_name="Пара")
	alter = models.IntegerField("Неделя(+/-)", default=0)
	
	def __str__(self):
		return self.teacher.name
