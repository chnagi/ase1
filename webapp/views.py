from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.template import loader,Context
import requests


def login(request):
	
	template=loader.get_template('webapp/login.html')
	context={}
	return HttpResponse(template.render(context,request))
def signup(request):
	time=""
	name=request.POST['username']
	email=request.POST["email"]
	roll_number=request.POST['roll_number']
	distance=request.POST['distance']
	velocity=request.POST['velocity']
	q=User(Name=name,email=email,Roll_no=roll_number,Distnace=distance,Velocity=velocity)
	q.save()
	#time=int(time)
	time=float(distance)/float(velocity)
	context={'k':time}
	template=loader.get_template('webapp/signup.html')
	
	return HttpResponse(template.render(context,request))
def index(request):
	q=User.objects.all()
	return HttpResponse(q)
# Create your views here.
