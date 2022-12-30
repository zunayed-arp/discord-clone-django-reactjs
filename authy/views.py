from django.shortcuts import render,get_object_or_404,redirect
from authy.forms import SignupForm, ChangePasswordForm, EditProfileForm
from django.contrib.auth.models import User
from authy.models import Profile
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required





def sideNavInfo(request):
    user = request.user
    nav_profile = None
    fans = None
    follows = None
    
  
  
def userProfile(request,username):
    user = get_object_or_404(User,username=username)
    profile = Profile.objects.get(user=user)
    template = loader.get_template('profile.html')
    
    context = {
        'profile':profile
    }
    
    return HttpResponse(template.render(context,request))




def Signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username,email=email,password=password)
            return redirect('edit-profile')
    else:
        form = SignupForm()
        
    context = {
        'form':form
    }
    
    return render(request,'registration/signup.html',context)

@login_required
def PasswordChange(request):
    user = request.user
    
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            user.set_password(new_password)
            user.save()       
    else:
        form = ChangePasswordForm(instance=user)
    
    context = {
        'form':form,
    }
    
    return render(request,'registration/change_password.html',context)


def PasswordChangeDone(request):
    return render(request,'change_password_done.html')



def EditProfile(request):
    user = request.user
    
    profile = Profile.objects.get(user__id=user)
    user_basic_info = User.objects.get(id=user)
    
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES,instance=profile)
        if form.is_valid():
            profile.picture = form.cleaned_data.get('picture')
            profile.bannner = form.cleaned_data.get('banner')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            profile.location = form.cleaned_data.get('location')
            profile.url = form.cleaned_data.get('url')
            profile.profile_info = form.cleaned_data.get('profile_info')
            profile.save()
            user_basic_info.save()
            return redirect('index')
    else:
        form = EditProfileForm(instance=profile)
    
    context = {
        'form':form,
    }
    return render(request,'registration/edit_profile.html',context)

    