from django.shortcuts import render , redirect

from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import User , Category, Tag , Post ,Comment
from .forms import PostForm  

@login_required 
def home_view(request):
    posts = Post.objects.all()
    context = {
        "posts":posts
    }
    return render(request , 'myblog/home.html',context=context)

@login_required
def create_view(request):
    if request.method=='POST':
        form = PostForm(request.Post , user = request.user)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm(user = request.user)
    
    return render(request , 'myblog/create_post.html', {'create_form':form})
