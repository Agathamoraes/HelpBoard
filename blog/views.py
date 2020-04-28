from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import  authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.http import HttpResponse

# Create your views here.

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required(login_url='/login/')
def post_list(request):
    return render(request, 'blog/post_list.html', {})

def header (request):
    return render (request, 'base_header.html')

def detail (request,title):
    posts = Post.objects.filter(title__icontains = title)
    return render (request,'detail.html', {'posts':posts})

def menu (request):
    search = request.GET.get('search')

    if search:
        posts = Post.objects.filter(title__icontains = search)
    else:
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/menu.html', {'posts': posts})


def footer (request):
    return render (request, 'base_footer.html')
def footer_avalia (request):
    return render (request, 'base_footer_avalia.html')


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

    