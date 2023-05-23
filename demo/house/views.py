from django.shortcuts import render, redirect
from .form import House_refer_form, Refer_form
from .models import Refer, House_refer
import string
import random
# Create your views here.


def home(request):

    return render(request, "home.html", )


def link(request):

    form = Refer_form()

    if request.method == "POST":
        form = Refer_form(request.POST)
        if form.is_valid():
            print(request.POST)
            a = Refer(name=request.POST['name'], link=''.join(
                random.choices(string.ascii_letters, k=7)))
            a.save()
            h = Refer.objects.get(name=name)
            return redirect('link display', link=h.link)
    context = {"form": form, "res": ''.join(
        random.choices(string.ascii_letters, k=7))}
    return render(request, "refer.html", context)


def name(request, link):
    h = Refer.objects.get(link=link)
    s = h.link
    context = {"s": s}
    return render(request, "link.html", context)


def form(request):
    form = House_refer_form()
    if request.method == "POST":
        form = House_refer_form(request.POST)
        if form.is_valid():
            o = request.POST["Referal_code"]
            list = Refer.objects.get(link=o)

            list.counter += 1
            list.save()
            form.save()
            return redirect("/house/")

    context = {'form': form}
    return render(request, "refer_house_form.html", context)
