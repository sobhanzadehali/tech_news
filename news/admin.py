from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Content)
admin.site.register(Topic)
admin.site.register(Comment)