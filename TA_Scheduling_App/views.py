from django.shortcuts import render
from django.views import View
from application.app import App



# Create your views here.
class Home(View):
  def get(self, request):
    return render(request, "index.html")

  def post(self, request):

    app = App()
    out = app.command(request.POST["command"])
    return render(request, "index.html", {"out": out})
