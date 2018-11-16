from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myhome(request):
    return render(request,'home.html')


def about(request):
    return render(request,'about.html')