from home.forms import TaskForm
from django.contrib import admin
from .models import *
from .forms import *

admin.site.register(Task)
# admin.site.register(TaskForm)
