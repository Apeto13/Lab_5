from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect


class LoginForm(forms.Form):

    username = forms.CharField(label='username')
    password = forms.CharField(
        label='password', widget=forms.PasswordInput(render_value=True))

class Person():
    def __init__(self,username,password):
        self.username = username
        self.password = password


def index(request):
    if "users" not in request.session:
        request.session["users"] = []
    users = request.session["users"]
    return render(request, "signin/index.html", {"users": users})


def add(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            person = Person(username=username,password=password)
            request.session["users"] += [person.username]
            return HttpResponseRedirect(reverse("signin:index"))
        else:
            return render(request, "signin/add.html", {'form': form})

    return render(request, "signin/add.html", {
        "form": LoginForm()
    })
