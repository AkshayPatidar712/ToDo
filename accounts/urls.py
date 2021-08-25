from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('login_user', views.login_user, name='login_user'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_user, name='logout'),

]
