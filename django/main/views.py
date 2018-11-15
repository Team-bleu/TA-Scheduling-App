from django.shortcuts import render
from django.views import View
from app import App


# Create your views here.
class Home(View):
  def get(self, request):
    return render(request, "main_temp/index.html")

  def post(self, request):
    app = App()
    out = app.command(request.POST["command"])
    return render(request, "main_temp/index.html", {"out": out})
