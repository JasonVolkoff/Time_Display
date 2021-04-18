from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime


def index(request):
    context = {
        "date": strftime("%b %d, %Y", gmtime()),
        "time": strftime("%H:%M %p", gmtime()),
    }
    return render(request, "index.html", context)


def time_display(request):
    return redirect("/")
