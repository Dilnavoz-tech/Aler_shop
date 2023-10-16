from django.urls import path

from accounts.views import SignInView, RegisterView, LogoutView

urlpatterns = [
    path('login', SignInView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('logout', LogoutView.as_view(), name='logout')
]