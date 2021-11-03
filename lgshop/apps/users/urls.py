# @ Time    : 2021/1/20 21:57
# @ Author  : JuRan
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # 注册
    path('register/', views.RegisterView.as_view(), name='register'),
]