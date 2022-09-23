
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect ('login')
    return render(request, 'users/register_form.html', {'form': form})


@login_required
def profile(request):
    return render (request, 'users/profile.html')

@login_required
def update(request):
    if request.method == "POST":
        user = request.user
        u_form = UserUpdateForm(request.POST, instance=request.user )
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect ('profile')
    else: 
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
    context = { 
               'u_form' : u_form, 
               'p_form': p_form 
    }
    return render  (request, 'users/update_form.html', context)