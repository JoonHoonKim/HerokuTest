from django.shortcuts import render, redirect

from django.contrib.auth.models import User#user만드는 함수들 가져와
from django.contrib import auth
# Create your views here.
def login(request):
    if request.method == "POST":#보안에 신경 썼니?
        user = auth.authenticate(request, username = request.POST['username'], password = request.POST['password'])#존재하니?
        if user is not None:
            auth.login(request, user)#로그인
            return redirect('blog')
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password'])#유저 만들어줘
                auth.login(request, user)#유저 로그인해줘
                return redirect('blog')
    return render(request, 'signup.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('blog')
    return render(request, 'signup.html')