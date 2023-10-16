from django.urls import path

from main.views import (HomeView,
                        ProfileView,
                        BlogView, PropertyGridView, AboutView,
                        )

urlpatterns = [
     path('', HomeView.as_view(), name='home'),
     path('profile', ProfileView.as_view(), name='profile'),
     path('blog', BlogView.as_view(), name='blog'),
     path('property', PropertyGridView.as_view(), name='property'),
     path('about', AboutView.as_view(), name='about'),
]