from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from blogs.forms import CommentForm
from blogs.models import Post, Comment


def posts(request):
    object_list = Post.objects.all()
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
    post = Post.objects.filter(id=pk).first()
    comments = Comment.objects.filter(post=post).all()

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
        'comments': comments,
    }
    return render(request, 'blogs/blog-single.html', context)
