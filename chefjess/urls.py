from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
  path('admin/', admin.site.urls),
  path('', include('index.urls')),
]
