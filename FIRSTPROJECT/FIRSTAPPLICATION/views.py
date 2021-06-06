from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hi")
def demo(request):
    return render(request, 'view.html')