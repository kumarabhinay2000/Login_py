from django.urls import path
from . import views
urlpatterns = [
    path('',views.main_page,name='main'),
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('welcome', views.welcome_view, name='welcome'),
    path('logout/',views.logout_view, name='logout'),
]
