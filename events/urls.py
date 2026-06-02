from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('register/', views.register, name='register'),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    path('user/', views.user_page, name='user'),

    path('profile/', views.profile, name='profile'),

    path('myevents/', views.myevents, name='myevents'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path(
        'register-event/<int:event_id>/',
        views.register_event,
        name='register_event'
    ),
]