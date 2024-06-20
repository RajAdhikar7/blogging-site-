from django.shortcuts import render , redirect , get_object_or_404

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
        form = PostForm(request.POST , user = request.user)
        if form.is_valid():
            post = form.save()
            return redirect('detail',id=post.pk)
    else:
        form = PostForm(user = request.user)
    
    return render(request , 'myblog/create_post.html', {'create_form':form})

@login_required 
def detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'myblog/detail_post.html', {'post': post}) 

@login_required
def add_comment(request ,post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method =='POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(content=content, author=request.user , post=post)
    return redirect('detail', id = post.id)