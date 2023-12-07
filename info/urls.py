# 正在部署的应用的名称
from django.urls import path
from . import views

app_name = 'info'

urlpatterns = [
    # path函数将url映射到视图
    path('home/', views.home, name='home'),
    path('notes/', views.notes, name='notes'),
    path('papers/', views.papers, name='papers'),
    path('ynu/', views.ynu, name='ynu'),
    path('lanping/', views.lanping, name='lanping'),
    path('closedFriends/', views.closedFriends, name='closedFriends'),
    path('misc/', views.misc, name='misc'),

]