from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("<h3>Hello world</h3>")
def hey(request):
	return HttpResponse("<h2>hey how u doing?</h2>")