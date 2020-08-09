from django.shortcuts import render,redirect
from .models import Job
from django.http import HttpResponse
from .forms import ContactForm
from .models import Contact
# Create your views here.
def home(request):
    jobs=Job.objects
    return render(request,'jobs/home.html',{'jobs':jobs})
    #return HttpResponse('<h1>Hi</h1>')

def contactView(request):
    if request.method == 'GET':
        return render(request, "jobs/success.html", {'form': ContactForm()})

    else:
        try:
            form = ContactForm(request.POST)
            newform = form.save(commit=False)
            user = User.objects.create_user(request.POST['username'],request.POST['email'],request.POST['subject'],request.POST['message'])
            user.save()
            newform.user = request.user
            newform.save()
            print(Success)
            return redirect ('success')
        except ValueError:
            return render(request, "jobs/success.html", {'form': ContactForm(),'error':'Bad data passed in. Try again.'})






