from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout


# Create your views here.

def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect('/login')
    return    render (request, 'index.html')

def loginuser(request):
    if request.method =='POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        print(username,password)
        #check if user has entered correct credentials
        user = authenticate(username==username, password==password)
        if user is not None:
            login( user)
            # A backend authenticated the credentials
            return redirect('/index')

        else:
            # No backend authenticated the credentials
            return render (request, 'login.html')
    return render (request, 'login.html')

def logoutuser(request):
    logout(request)

    return redirect('/login')
