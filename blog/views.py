from django.shortcuts import render

def Home(request):
    return render(request,'blog/home.html')

def About(request):
    return render(request,'blog/about.html')