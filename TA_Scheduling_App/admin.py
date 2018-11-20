from django.contrib import admin
from .models import Account, Class, Relationship

# Register your models here.
admin.site.register(Account)
admin.site.register(Class)
admin.site.register(Relationship)
