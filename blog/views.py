from django.shortcuts import render,HttpResponseRedirect

def Home(request):
    return render(request,'blog/home.html')

def About(request):
    return render(request,'blog/about.html')


def Contact(request):
    return render(request,'blog/contact.html')


def Dashboard(request):
    return render(request,'blog/dashboard.html')


def UserLogout(request):
    return HttpResponseRedirect('/')


def Signup(request):
    return render(request,'blog/signup.html')


def UserLogin(request):
    return render(request,'blog/login.html')