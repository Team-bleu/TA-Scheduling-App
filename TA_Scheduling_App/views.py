from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from application.app import App


# Create your views here.
app = App()

class Main(View):
    def get(self, request):
        return render(request, "main.html")

    def post(self, request):
        out = app.command(request.POST["command"])
        return render(request, "main.html", {"out": out})


class Login(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        command = "login " + username + " " + password
        out = app.command(command)
        if out != username + " logged in.":
            return render(request, "login.html", {"out": out})
        return redirect('main/', request)
