from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    log = forms.CharField(label="user")


def index(request):
    if "users" in request.session:
        request.session["users"] = []
    return render(request, "signin/index.html", {"users": request.session["users"]})


def add(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data["user"]
            users.append(user)
            return HttpResponseRedirect(reverse("signin:index"))
        else:
            return render(request, "signin/add.html", {'form': form})

    return render(request, "signin/add.html", {
        "form": LoginForm()
    })
