from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.shortcuts import render,redirect

from ..forms import CustomUserForm


def register(request):

    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registered Succesfully! Login to Continue')
            return redirect('/login')
    context={'form':form}

    return render(request,'auth/register.html',context)

def loginweb(request):

    if request.user.is_authenticated:
        messages.warning(request,'You are already Logged in')
        return redirect('/')
    else:

        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')

            user = authenticate(request,username =name,password = passwd)

            if user is not None:
                login(request,user)
                messages.success(request,'Logged in successfully')
                return redirect('/')
            else:
                messages.error(request,'Invalid username or password')
                return redirect('/login')
        return render(request,'auth/loginweb.html')

def logoutweb(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'Logged out successfully')
        return redirect('/')
