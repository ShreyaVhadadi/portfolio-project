from django.shortcuts import render,redirect
from .models import Job
from django.http import HttpResponse
from .forms import ContactForm
# Create your views here.
def home(request):
    jobs=Job.objects
    return render(request,'jobs/home.html',{'jobs':jobs})
    #return HttpResponse('<h1>Hi</h1>')

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(name,subject, message, from_email, ['svhadadi@stevens.edu'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

    return render(request, "jobs/success.html", {'form': form})


