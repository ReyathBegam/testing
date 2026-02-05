from django.urls import path
from .views import HomeView, UploadView, register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('upload/', UploadView.as_view(), name='upload'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
