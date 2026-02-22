from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages   # for showing warnings


# Signup
def SignupPage(request):
    if request.user.is_authenticated:
        messages.warning(request, "You must logout before signing up a new account.")
        return redirect('home')

    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        errors = {}

        if User.objects.filter(username=uname).exists():
            errors['username'] = "This username is already taken. Please choose another one."

        if User.objects.filter(email=email).exists():
            errors['email'] = "This email is already taken. Please choose another one."

        if pass1 != pass2:
            errors['password'] = "Your password and confirm password do not match!!"

        if errors:
            context = {
                'errors': errors,
                'form_data': {
                    'username': uname,
                    'email': email
                }
            }
            return render(request, 'account/signup.html', context)

        my_user = User.objects.create_user(uname, email, pass1)
        my_user.save()
        return redirect('LoginPage')

    return render(request, 'account/signup.html')

# Login
def LoginPage(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in. Please logout first.")
        return redirect('home')

    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Username or Password is incorrect!!!"

    return render(request, 'account/login.html', {'error_message': error_message})

# Logout
@login_required(login_url='LoginPage')
def LogoutPage(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')

def custom_404(request, exception):
    return render(request, 'errors/404.html', status=404)

def custom_400(request, exception):
    return render(request, 'errors/400.html', status=400)

def custom_403(request, exception):
    return render(request, 'errors/403.html', status=403)

def custom_500(request):
    return render(request, 'errors/500.html', status=500)
