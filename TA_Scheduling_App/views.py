from django.shortcuts import render, redirect
from django.views import View
from application.app import App


# Create your views here.
class Home(View):
  def get(self, request):
    return render(request, "login.html")

  def post(self, request):
    app = App()
    out = app.command(request.POST["command"])
    if out is "logged out.":
        return redirect('', permanent=True)
    return render(request, "index.html", {"out": out})

class Login(View):
  def get(self, request):
    return render(request, "login.html")

  def post(self, request):
    username = request.POST["username"]
    password = request.POST["password"]
    command = "login " + username + " " + password
    app = App()
    out = app.command(command)
    if out is not username + " logged in.":
        return render(request, "login.html", {"out": out})
    return redirect('main/', permanent=True)
