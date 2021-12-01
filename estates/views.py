from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from blogs.models import Post
from estates.models import Estate


def main_page(request):
    latest_estates = Estate.objects.all().order_by('-date_created')[:6]
    latest_news = Post.objects.all().order_by('-date_created')[:6]
    chosen_estates = Estate.objects.all().filter(chosen=True)

    context = {
        'last_six_estates': latest_estates,
        'latest_news': latest_news,
        'chosen_estates': chosen_estates
    }
    return render(request, 'estates/index.html', context)


def all_properties(request):
    object_list = Estate.objects.all()
    paginator = Paginator(object_list, 6)
    page = request.GET.get('page')
    try:
        estates = paginator.page(page)
    except PageNotAnInteger:
        estates = paginator.page(1)
    except EmptyPage:
        estates = paginator.page(paginator.num_pages)

    context = {
        'page': page,
        'estates': estates,
        'title': 'Our All Properties'
    }
    return render(request, 'estates/property-grid.html', context)


def new_properties(request):
    new_estates = Estate.objects.all().order_by('date_created')

    context = {
        'estates': new_estates,
        'title': 'Our New to Old Properties'
    }
    return render(request, 'estates/property-grid.html', context)


def rent_properties(request):
    rent_estates = Estate.objects.all().filter(status='Rent')

    context = {
        'estates': rent_estates,
        'title': 'Our Rent Properties'
    }
    return render(request, 'estates/property-grid.html', context)


def sale_properties(request):
    sale_estates = Estate.objects.all().filter(status='Sale')

    context = {
        'estates': sale_estates,
        'title': 'Our Sale Properties'
    }
    return render(request, 'estates/property-grid.html', context)


def estate_detail(request, pk):
    estate = Estate.objects.filter(id=pk).first()

    context = {
        'estate': estate
    }
    return render(request, 'estates/property-single.html', context)


