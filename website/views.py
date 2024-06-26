from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('User is valid')
            login(request, user)
            messages.success(request, 'You are now logged in!')
            return redirect('home')
        else:
            print('Invalid credentials!')
            messages.error(request, 'Invalid credentials!')
            return redirect('home')
    else:
        return render(request, 'home.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'You are now logged out!')
    return render(request, 'home.html')

def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            messages.success(request, f'Your account has been created! Welcome {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
        return render(request,'register.html', {'form': form})
    return render(request,'register.html', {'form': form})
