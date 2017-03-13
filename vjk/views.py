from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def search(request):
	return HttpResponse("this page will allow you to search through tables.")

def home(request):
	return HttpResponse("you can choose what you want to do.")

def email(request):
	return HttpResponse("send email to different people.")

def edit(request):
	return HttpResponse("edit entries in tables.")

def add(request):
	return HttpResponse("add entries in tables.")

def delete(request):
	return HttpResponse("delete entries in tables.")