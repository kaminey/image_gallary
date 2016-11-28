from django.http import HttpResponse
from django.shortcuts import render

def image_gallary(request):
	return render(request, "image_gallary.html")
