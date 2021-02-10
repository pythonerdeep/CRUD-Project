from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm

from .models import Registration
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def register(request):
    form=RegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        em=form.cleaned_data.get('email')
        subject='Welcome to my CRUD'
        message='This is the CRUD system, it is very useful for manage many data.' \
                'Thanks for registering on my site, I hope it is helpful for you.' \
                'Thank You :)'
        email_from=settings.EMAIL_HOST_USER
        recipient_list=[em]
        send_mail(subject, message, email_from, recipient_list)
        return redirect('/login')
    return render(request,'register.html',{'form':form})

def login(request):
    form=LoginForm(request.POST or None)
    if form.is_valid():
        email1=form.cleaned_data.get('email')
        password1=form.cleaned_data.get('password')
        print(email1,password1)

        r=Registration.objects.filter(email=email1,password=password1)
        if r:
            request.session['em']=email1
            print('data match')
            return redirect('/dashboard')
        else:
            print('data not match')
    return render(request,'login.html',{'form':form})

def dashboard(request):
    em=request.session.get('em')
    user=Registration.objects.get(email=em)
    return render(request,'ldashboard.html',{'record':user})

def logout(request):
    del request.session['em']
    return redirect('login/')

def home(request):
    return render(request,'home.html')