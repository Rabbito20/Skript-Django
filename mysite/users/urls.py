from django.contrib import admin
from django.urls import path
#from .views import views
from . import views
from django.contrib.auth import views as auth_views

#   users urls

urlpatterns = [
    path('register/', views.register, name='register'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

]
