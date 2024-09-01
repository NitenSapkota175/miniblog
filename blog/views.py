from django.shortcuts import render,HttpResponseRedirect
from . forms import SignupForm,LoginForm,PostForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from . models import Post
from django.contrib.auth.models import Group

def Home(request):
    blogs = Post.objects.all()

    return render(request,'blog/home.html',{'blogs' : blogs})

def About(request):
    return render(request,'blog/about.html')


def Contact(request):
    return render(request,'blog/contact.html')


def Dashboard(request):
   
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        ip = request.session.get('ip',0)
        return render(request,'blog/dashboard.html',{'posts' : posts , "groups" : gps,"full_name" : full_name , 'ip' : ip})
    else:
        return HttpResponseRedirect('/login/')

def UserLogout(request):
    return HttpResponseRedirect('/')


def UserSignup(request):
    if not request.user.is_authenticated: 
        if request.method == 'POST':
                form = SignupForm(request.POST)
                if form.is_valid():
                    messages.success(request,'Congrats! You have become an author! Login to create an blog post')
                    user = form.save()
                    group = Group.objects.get(name="Author")
                    user.groups.add(group)
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
                    return HttpResponseRedirect('/dashboard/')   

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
        

# add new post
def AddPost(request):

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                ftitle = form.cleaned_data.get('title')
                fdesc = form.cleaned_data.get('desc')
                pst = Post(title=ftitle,desc=fdesc)
                pst.save()
                messages.success(request,'You have created the post')
                return HttpResponseRedirect('/dashboard/')

        else:
            form = PostForm()
        return render(request,'blog/addpost.html',{'form' : form})
    
    else:
        return HttpResponseRedirect('/login/')
    
#update post

def UpdatePost(request,pk):

    if request.user.is_authenticated:
        post = Post.objects.get(id=pk)
        if request.method == 'POST':
            form = PostForm(request.POST,instance=post)
            if form.is_valid():
                form.save()
                messages.success(request,'You have update the post')
                return HttpResponseRedirect('/dashboard/')


        else:
            form = PostForm(instance=post)

        return render(request,'blog/updatepost.html',{'form' : form})
    
    else:
        return HttpResponseRedirect('/login/')



def DeletePost(request,pk):
     if request.user.is_authenticated:
        if request.method == 'POST':
            pst = Post.objects.get(id=pk)
            pst.delete()
            messages.success(request,'You have deleted Post')
            return HttpResponseRedirect('/dashboard/')
    
     else:
        return HttpResponseRedirect('/login/')