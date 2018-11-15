from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from main import views
from main.views import Home

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  path('', Home.as_view()),
]
