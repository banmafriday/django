from django.shortcuts import render
from django.views import View


class RegisterView(View):

    def get(self, request):
        """提供用户注册页面"""
        return render(request, 'register.html')