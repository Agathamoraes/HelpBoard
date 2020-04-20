from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import  authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/login/')
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'blog/post_list.html', {})

def logout_user (request):
    logout (request)
    return redirect ('/login/')

def login_user (request):
    return render (request, 'login.html')
@csrf_protect
def submit_login (request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate (username = username, password = password)
        if user is not None:
            login (request, user)
            return redirect ('/')
        else:
            messages.error (request, 'Usuário ou senha Inválido. Tente novamente')
    return redirect ('/login/')