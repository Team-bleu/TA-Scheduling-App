from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from application.app import App


# Create your views here.
app = App()

class Main(View):
    def get(self, request):
        help = self.getHelp()
        role = self.getRole()
        return render(request, "main.html", {"help": help, "role": role})

    def post(self, request):
        help = self.getHelp()
        role = self.getRole()
        out = app.command(request.POST["command"])
        if out == "Quiting session." or out == "logged out.":
            return redirect('/', request)
        return render(request, "main.html", {"out": out, "help": help, "role": role})

    def getRole(self):
        return app.commands.getLogger().getRole()

    def getHelp(self):
        return app.command("help")


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


class Edit(View):
    def get(self, request):
        info = app.command("show")
        return render(request, "edit.html", {"info": info})

    def post(self, request):
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        address = request.POST["address"]
        officehours = request.POST["officehours"]

        username = app.commands.getLogger().getUsername()

        editstring = "edit " + username
        if len(firstname) is not 0:
            editstring = editstring + " firstname " + firstname
        if len(lastname) is not 0:
            editstring = editstring + " lastname " + lastname
        if len(phone) is not 0:
            editstring = editstring + " phone " + phone
        if len(email) is not 0:
            editstring = editstring + " email " + email
        if len(address) is not 0:
            editstring = editstring + " address " + address
        if len(officehours) is not 0:
            editstring = editstring + " officehours " + officehours

        app.command(editstring)

        info = app.command("show")
        return render(request, "edit.html", {"info": info})
