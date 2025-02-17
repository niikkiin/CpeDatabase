from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from account.forms import UserForm, UserProfileInfoForm
from django.contrib import messages

# for Login
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

class LoginView(TemplateView):
    template_name = 'account/login.html'

def register(request):
    
    registered = False
    
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                
            profile.save()
            
            registered = True
        
        else:
            print(user_form.errors, profile_form.errors)
    
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        
    return render(request, 'account/register.html', {'user_form':user_form, 
                                                'profile_form':profile_form,
                                                'registered':registered})
    
def user_login(request):

    user = request.user

    if user.is_authenticated:
        return redirect('home:home')
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                print('success')
                return HttpResponseRedirect(reverse('home:home'))
            else:
                return HttpResponse("Account Not Active")
            
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username, password))
            # return HttpResponse("Invalid Login Details Supplied!")
            messages.error(request, 'That user account does not exist.')
            return redirect('account:user_login')
        
    else:
        return render(request, 'account/login.html', {})
    
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('account:user_login'))