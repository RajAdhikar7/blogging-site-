from django.shortcuts import render,redirect
from django.contrib import messages

from django.contrib.auth import authenticate,login , logout
from django.contrib.auth.forms import AuthenticationForm 

from .forms import UserRegistrationForm




# Create your views here.
def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home') 
            else:
                login_form.add_error('Authentication failed. Please try again.')
    else:
        login_form = AuthenticationForm()  # Create an empty form for GET requests
        
    context = {
        'login_form': login_form
    }
    return render(request, 'accounts/login.html', context)
            

def register_view(request):
    if request.method == 'POST':
        register_form = UserRegistrationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.set_password(register_form.cleaned_data['password'])
            user.save()
            username = register_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/login')  # Update this to your login view or homepage
    else:
        register_form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'register_form': register_form}) 


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('/login/')
    return render(request,"accounts/logout.html",{})