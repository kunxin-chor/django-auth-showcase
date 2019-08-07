from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import auth, messages
from .forms import UserLoginForm

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def logout(request):
    """Logouts the user"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('index'))


def login(request):
    """Returns the login page"""
    if request.method == 'POST':
        pass
    else:
        login_form = UserLoginForm
        return render(request, 'login.html', {
            'form':login_form
        })