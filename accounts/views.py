from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.


def login_user(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('task')
        else:
            return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task')
        else:
            return render(request, 'signup.html', {'form': form})


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login_user')
