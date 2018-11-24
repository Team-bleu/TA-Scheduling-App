from django.shortcuts import render
from django.views import View
from application.app import App
#from application.tests.unit_tests import mainUnitTests


# Create your views here.
class Home(View):
  def get(self, request):
    return render(request, "index.html")

  def post(self, request):
    #mainUnitTests.main_tests()
    app = App()
    out = app.command(request.POST["command"])
    return render(request, "index.html", {"out": out})
