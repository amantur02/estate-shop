from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.shortcuts import render, redirect

from estates.models import Estate
from .forms import ProfileRegistrationForm, ProfileUpdateForm
from .models import Profile


def register(request):
    error = ''
    if request.method == 'POST':
        form = ProfileRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            error = 'Form is not valid, try again'
    form = ProfileRegistrationForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('main_page')
    form = ProfileUpdateForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'users/profile.html', context)


def profile_detail(request, pk):
    profile = Profile.objects.filter(id=pk).first()
    estates = Estate.objects.filter(author=profile)

    context = {
        'profile': profile,
        'estates': estates
    }
    return render(request, 'users/user-single.html', context)


def about(request):
    return render(request, 'users/agent-single.html')
