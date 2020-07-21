from django.shortcuts import render
from .models import Job
from django.http import HttpResponse
# Create your views here.
def home(request):
    jobs=Job.objects
    return render(request,'jobs/home.html',{'jobs':jobs})
    #return HttpResponse('<h1>Hi</h1>')