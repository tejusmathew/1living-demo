from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import random
import string
from house.models import Refer, House_refer
# Create your views here.


@login_required
def Homepage(request):
    h = request.user
    if request.user is not None:
        l = Refer.objects.get(name=h.username)
    else:
        return HttpResponse("404")

    context = {"x": l.link, "s": l.name}

    return render(request, "h.html", context)


def Register(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        password = request.POST.get('pass_word')
        email = request.POST.get('email')
        a = Refer(name=request.POST['fname'], link=''.join(
            random.choices(string.ascii_letters, k=7)))
        a.save()
        new_user = User.objects.create_user(fname, email, password)
        new_user.first_name = fname
        new_user.save()
        return redirect('login-page')
    return render(request, 'register.html', {})


def Login(request):
    if request.method == "POST":
        username = request.POST.get('fname')
        pass_word = request.POST.get('pass_word')
        user = authenticate(request, username=username, password=pass_word)
        if user is not None:
            login(request, user)
            return redirect('Home-page')
        else:
            return HttpResponse("Error,user does not exsit")

    return render(request, "login.html", {})


def logoutuser(request):
    logout(request)
    return redirect('login-page')


def Register_ref(request, link):
    x = Refer.objects.get(link=link)
    if x is not None:
        if request.method == "POST":
            fname = request.POST.get('fname')
            password = request.POST.get('pass_word')
            email = request.POST.get('email')
            a = Refer(name=request.POST['fname'], link=''.join(
                random.choices(string.ascii_letters, k=7)), Reffered_by=x.name)
            x.counter += 1
            x.save()
            a.save()
            new_user = User.objects.create_user(fname, email, password)
            new_user.first_name = fname

            new_user.save()
            return redirect('login-page')
    else:
        return HttpResponse("404")
    return render(request, 'reg_ref.html', {})
