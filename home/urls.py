from django.urls import path
from . import views

urlpatterns = [

    path('task', views.taskAdd, name='task'),
    path('list/', views.taskList, name='list'),
    path('<int:id>/', views.taskUpdate, name='update'),
    path('delete/<int:id>', views.taskDelete, name='delete')
]
