from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import  authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required(login_url='/login/')
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'blog/post_list.html', {})

def index2 (request):
    return render (request, 'index2.html')

def index3 (request):
    return render (request, 'index3.html')
def index4 (request):
    return render (request, 'index4.html')
def index5 (request):
    return render (request, 'index5.html')
def index7 (request):
    return render (request, 'index7.html')
def index6 (request):
    return render (request, 'index6.html')
def index8 (request):
    return render (request, 'index8.html')
def index9 (request):
    return render (request, 'index9.html')
def index10 (request):
    return render (request, 'index10.html')
def index11 (request):
    return render (request, 'index11.html')
def index12 (request):
    return render (request, 'index12.html')

def header (request):
    return render (request, 'base_header.html')


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

    