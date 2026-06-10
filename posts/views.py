from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from django.template import loader
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Post
from .forms import PostForm

def posts(request):
    posts = Post.objects.all()
    sports_news = posts.filter(category='sports')
    tech_news = posts.filter(category='technology')
    business_news = posts.filter(category='business')
    entertainment_news = posts.filter(category='entertainment')
    
    template = loader.get_template('list.html')
    content = {
        'news': posts,
        'sports_news': sports_news,
        'tech_news': tech_news,
        'business_news': business_news,
        'entertainment_news': entertainment_news,
    }
    return HttpResponse(template.render(content, request))

@login_required(login_url='/posts/login/')
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(f'/posts/details/{post.id}')
    else:
        form = PostForm()
    return render(request, 'create.html', {'form': form})

def details(request, id):
    post = get_object_or_404(Post, id=id)
    template = loader.get_template('details.html')
    content = {
        'post': post,
        'id': id,
    }
    return HttpResponse(template.render(content, request))

@login_required(login_url='/posts/login/')
def edit(request, id):
    post = get_object_or_404(Post, id=id)
    
    # Check auth
    if post.author and post.author != request.user:
        return HttpResponseForbidden("You are not authorized to edit this post.")
        
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(f'/posts/details/{post.id}')
    else:
        form = PostForm(instance=post)
    return render(request, 'create.html', {'form': form, 'post': post})

@login_required(login_url='/posts/login/')
def delete(request, id):
    post = get_object_or_404(Post, id=id)
    
    # Check auth
    if post.author and post.author != request.user:
        return HttpResponseForbidden("You are not authorized to delete this post.")
        
    post.delete()
    return redirect('/posts')

@login_required(login_url='/posts/login/')
def dashboard(request):
    user_posts = Post.objects.filter(author=request.user)
    template = loader.get_template('dashboard.html')
    content = {
        'news': user_posts,
    }
    return HttpResponse(template.render(content, request))

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/posts')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/posts')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/posts')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('/posts')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/posts')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
