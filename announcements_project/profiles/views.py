from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import ProfileForm
from .models import Profile

# Create your views here.
@login_required
def update_profile(request):
    profile, created = Profile.objects.get_or_create(user = request.user)
    if request.method == "GET":
        form = ProfileForm(instance = profile)
    elif request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance = profile)
        if form.is_valid():
            form.save()
            return redirect('profile_edit')
        
    return render(request, 'profiles/edit_profile.html', { 'form' : form, 'profile' : profile })

@login_required
def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles/profile_list.html', { 'profiles' : profiles })