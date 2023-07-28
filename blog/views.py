from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import BlogPost, Video
#User signup
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
#add blog post to the website
@login_required
def add_blog_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        BlogPost.objects.create(title=title, content=content, author=request.user)
        return redirect('blog_list')
    return render(request, 'add_blog_post.html')

@login_required
def add_video(request):
    if request.method == 'POST':
        title = request.POST['title']
        video_url = request.POST['video_url']
        Video.objects.create(title=title, video_url=video_url, author=request.user)
        return redirect('video_list')
    return render(request, 'add_video.html')

@login_required
def blog_list(request):
    blogs = BlogPost.objects.filter(is_approved=True)
    return render(request, 'blog_list.html', {'blogs': blogs})

@login_required
def video_list(request):
    videos = Video.objects.filter(is_approved=True)
    return render(request, 'video_list.html', {'videos': videos})