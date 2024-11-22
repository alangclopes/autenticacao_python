from django.urls import path
from .views import login_view, logout_view, register_view, home_view, index_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('home/', home_view, name='home'),
    path('', index_view, name='index'),
]