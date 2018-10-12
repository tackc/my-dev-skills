from django.shortcuts import render
from .models import User, Skill, Note
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Class-Based Views (CBVs)
class SkillCreate(CreateView):
    model = Skill
    fields = ['name', 'description', 'skilllevel']

# Create your views here.
def myskills(request):
    return render(request, 'myskills.html')

def addskill(request):
    return render(request, 'addskill.html')

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        # if post, then authenticate (user submitted username and password)
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The account has been disabled.")
                    return HttpResponseRedirect('/')
            else:
                print("The username and/or password is incorrect.")
                return HttpResponseRedirect('/')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

@login_required
def profile(request, username):
    if username == request.user.username:
        user = User.objects.get(username=username)
        skills = Skills.objects.filter(user=user)
        return render(request, 'profile.html', {'username': username, 'skills': skills})
    else:
        return HttpResponseRedirect('/')
