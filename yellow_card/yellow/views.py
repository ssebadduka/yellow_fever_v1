from django.shortcuts import render,redirect
from .models import personal_details
from django.views.generic import DetailView,ListView,UpdateView,CreateView,DeleteView
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.contrib.auth.models import User,auth




class IndexView(ListView):
    template_name="index.html"
    context_object_name = "yellow"
    model = personal_details
    
# class LoginView(ListView):
#     template_name="account/login.html"
#     context_object_name = "login"
    
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    
    else:
        return render (request,'login.html')  

def logout(request):
    auth.logout(request)
    return redirect('/')
    