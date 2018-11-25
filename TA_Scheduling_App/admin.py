from django.contrib import admin
from .models import Account, Class, Relationship, Lab, Instructor, TA

# Register your models here.
admin.site.register(Account)
admin.site.register(Class)
admin.site.register(Relationship)
admin.site.register(Lab)
admin.site.register(Instructor)
admin.site.register(TA)
