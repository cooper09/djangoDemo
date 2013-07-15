from django.http import HttpResponse
from proj1.models import table1

def start(request):
	return HttpResponse("Start Page...")

def hello(request):
	return HttpResponse("Hello World")

def testread(request):
	testList = table1.objects.all()
	print testList
	return HttpResponse("test read")