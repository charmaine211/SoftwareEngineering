from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def login_user(request):
    """
    Let's user login after filling in an existing username with it's matching password. 

    Args:
        request.POST['username']: Username
        request.POST['password']: Password

    Returns:
        Returns redirect to ou/index.html after successfully login in
        Otherwise returns authenticate/login.html
    """
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            # Clear messages
            storage = messages.get_messages(request)
            for message in storage:
                message.used = True

            messages.success(request, ("Login not correct, try again"))

            return render(request, 'authenticate/login.html', {})

    else:
        return render(request, 'authenticate/login.html', {})


def logout_user(request):
    """
    Let's user logout.

    Args:
        request

    Returns:
        Returns redirect to ou/index.html
    """
    logout(request)

    return redirect('index')


def register_user(request):
    """
    Let's user register and login with the registered user information.

    Args:
        request.POST['username']: Username
        request.POST['password1']: Password

    Returns:
        Returns redirect to ou/index.html after successfully registering and login in
        Otherwise returns authenticate/register_user.html
    """
    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)

            # Clear messages before diplaying
            storage = messages.get_messages(request)
            for message in storage:
                message.used = True

            messages.success(request, ("Registration successful"))

            return redirect('index')
    else:
        form = UserCreationForm()

    return render(request, 'authenticate/register_user.html', {'form': form})
