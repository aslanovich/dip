from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from pages.models import *
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.template import RequestContext

def user_login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('administrator/b1')
			else:
				return HttpResponse("Your account is disabled.")
		else:
			c = {'error': True}
			c.update(csrf(request))
			return render_to_response('pages/admin-login.html', c)
	else:
		if request.user.is_authenticated():
			return HttpResponseRedirect('administrator/b1')
		variables = RequestContext(request, { })
		return render_to_response('pages/admin-login.html', variables)

# Выход из системы
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('login')

@login_required
def administratorView(request, course):
	learningPlans = LearningPlan.objects.filter(course__number=course)
	audiences = Audience.objects.all()
	teachers = Teacher.objects.all()
	subjects = Subject.objects.all()
	days = Day.objects.all()
	pairs = Pair.objects.all()
	groups = Group.objects.filter(course__number=course)
	return render(request, 'pages/admin.html', {'plans': learningPlans, 'audiences': audiences, 'teachers': teachers, 'subjects': subjects, 
		'groups': groups, 'days': days, 'pairs': pairs, 'course': course})

def clientView(request, course):
	learningPlans = LearningPlan.objects.filter(course__number=course)
	audiences = Audience.objects.all()
	teachers = Teacher.objects.all()
	subjects = Subject.objects.all()
	days = Day.objects.all()
	pairs = Pair.objects.all()
	groups = Group.objects.filter(course__number=course)
	return render(request, 'pages/client.html', {'plans': learningPlans, 'audiences': audiences, 'teachers': teachers, 'subjects': subjects, 
		'groups': groups, 'days': days, 'pairs': pairs, 'course': course})

def createPlan(request):
	if request.method == 'POST':
		planId = request.POST.get('planId')
		deletePlan = request.POST.get('deletePlan')
		if planId:
			plan = LearningPlan.objects.get(id=planId)
		if deletePlan:
			plan.delete()
			return HttpResponse(status=200)

		teacherName = request.POST.get('teacher')
		teacher = Teacher.objects.get(name=teacherName)
		subjectTitle = request.POST.get('subject')
		subject = Subject.objects.get(title=subjectTitle)
		courseNumber = request.POST.get('course')
		course = Course.objects.get(number=courseNumber)
		groupNumber = request.POST.get('group')
		group = Group.objects.get(number=groupNumber)
		audienceTitle = request.POST.get('audience')
		audience = Audience.objects.get(title=audienceTitle)
		dayEng = request.POST.get('day')
		day = Day.objects.get(titleEng=dayEng)
		pairNumber = request.POST.get('pair')
		pair = Pair.objects.get(pair=pairNumber)
		alter = request.POST.get('alter')

		if planId:
			plan = LearningPlan.objects.get(id=planId)
			plan.teacher = teacher
			plan.subject = subject
			plan.course = course
			plan.group = group
			plan.audience = audience
			plan.day = day
			plan.pair = pair
			plan.alter = alter
			plan.save()
		else:
			LearningPlan.objects.get_or_create(
				teacher = teacher,
				subject = subject,
				course = course,
				group = group,
				audience = audience,
				day = day,
				pair = pair,
				alter = alter
				)

		return HttpResponse(23, status=200)
