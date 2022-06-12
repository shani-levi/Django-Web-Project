from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as logins
from django.contrib.auth import logout as logouts


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            logins(request, user)
            return redirect('main_home_page')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/sign_up.html', {"form": form})


def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            logins(request, user)
            return redirect('main_home_page')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/sign_in.html', {"form": form})


def logout(request):
    logouts(request)
    return redirect('main_home_page')