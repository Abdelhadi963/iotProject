from django.urls import path
from . import views

urlpatterns =[
    path('',views.index, name='index'),
    path('sign-up',views.register,name='sign-up'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('clima-monitoring',views.dashboard,name='dashboard'),
    path('dashboard',views.dashborad_views,name='dashboard-views')
]