from django.shortcuts import render,HttpResponseRedirect
from . forms import SignupForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from . models import Post
def Home(request):
    blogs = Post.objects.all()

    return render(request,'blog/home.html',{'blogs' : blogs})

def About(request):
    return render(request,'blog/about.html')


def Contact(request):
    return render(request,'blog/contact.html')


def Dashboard(request):

    if request.user.is_authenticated:
        return render(request,'blog/dashboard.html')
    else:
        return HttpResponseRedirect('/login/')

def UserLogout(request):
    return HttpResponseRedirect('/')


def UserSignup(request):
    if not request.user.is_authenticated: 
        if request.method == 'POST':
                form = SignupForm(request.POST)
                if form.is_valid():
                    messages.success(request,'You have sccuessfully created your account , please login!')
                    form.save()
                    return HttpResponseRedirect('/login/')

        else:
            form  = SignupForm()
        return render(request,'blog/signup.html',{'form' : form})

    else:
        return HttpResponseRedirect('/')
    

def UserLogin(request):

    if not request.user.is_authenticated: 
        if request.method == 'POST': 
            form = LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data.get('username')
                passwd = form.cleaned_data.get('password')
                user = authenticate(username=uname,password=passwd)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/')   

        else:
            form = LoginForm()
        return render(request,'blog/login.html',{'form' : form})
    
    else:
        return HttpResponseRedirect('/')
    

def UserLogout(request):
        if request.user.is_authenticated:
            logout(request)
            return HttpResponseRedirect('/login/')
        else:
            return HttpResponseRedirect('/login/')