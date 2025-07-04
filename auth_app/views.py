from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('bookstore:bookstore-index')
    else:
        if request.method == "POST":
            name= request.POST.get('username')
            password=request.POST.get('password')
            print(name,password)
            user= authenticate(username=name,password=password)
            if user is not None:
                login(request,user)
                if request.GET.get('next') is not None:
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('bookstore:bookstore-index')
            else:
                messages.info(request, "username or password is incorrect")
    return render(request,'login.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('bookstore:bookstore-index')
    else:
        signup_form = UserForm()
        if request.method == 'POST':
            signup_form = UserForm(request.POST)
            if signup_form.is_valid():
                signup_form.save()
                msg = "User account created for username: " + signup_form.cleaned_data.get('username')
                messages.info(request, msg)
                return redirect('login')
    
    context = {"signup_form": signup_form}
    return render(request, 'signup.html', context=context)
def log_out(request):
    logout(request)
    return redirect('login.html')