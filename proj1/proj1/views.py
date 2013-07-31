from django.http import HttpResponse
from proj1.models import Line

from django.shortcuts import render_to_response

def start(request):
	return HttpResponse("Start Page...")

def hello(request):
	return HttpResponse("Hello World")

def testread(request):
	#testList = Table12.objects.all()
	#print testList
	#return HttpResponse("Test Stuff goes here...")
	return render_to_response('proj1/home.html', {'lines': Line.objects.all()})