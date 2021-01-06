from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login


# Create your views here.
def register(req):
    if req.method == 'POST':
        form = RegistrationForm(req.POST)
        if form.is_valid():
            form.save()
            username = req.POST['username']
            password = req.POST['password1']
            user = authenticate(req, username=username, password=password)
            login(req, user)
            return redirect('apk-home')

    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(req, 'users/register.html', context)