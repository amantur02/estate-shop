from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect

from blogs.forms import CommentForm, PostCreateUpdateForm
from blogs.models import Post, Comment


def posts(request):
    object_list = Post.objects.all().order_by('-date_created')
    paginator = Paginator(object_list, 6)
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    context = {
        'page': page,
        'blogs': blogs
    }
    return render(request, 'blogs/blog-grid.html', context)


def post_detail(request, pk):
    author = False

    post = Post.objects.filter(id=pk).first()
    comments = Comment.objects.filter(post=post).all()

    if request.user == post.author:
        author = True

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
    form = CommentForm()

    context = {
        'post': post,
        'form': form,
        'author': author,
        'comments': comments,
    }
    return render(request, 'blogs/blog-single.html', context)


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostCreateUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts')
    form = PostCreateUpdateForm()
    context = {
        'form': form
    }
    return render(request, 'blogs/post_create.html', context)


def post_update(request, pk):
    post = Post.objects.filter(id=pk).first()
    if request.method == 'POST':
        form = PostCreateUpdateForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('my_posts')
    form = PostCreateUpdateForm(instance=post)
    return render(request, 'blogs/post_update.html',
                  context={'post': post, 'form': form})


def post_delete(request, pk):
    post = Post.objects.filter(id=pk).first()
    post.delete()
    return redirect('my_posts')


@login_required
def my_posts(request):
    object_list = Post.objects.filter(author=request.user)
    paginator = Paginator(object_list, 6)
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    context = {
        'page': page,
        'blogs': blogs
    }
    return render(request, 'blogs/blog-grid.html', context)
