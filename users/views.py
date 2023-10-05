from django.conf import settings
from django.contrib import messages
from django.contrib.auth import SESSION_KEY, BACKEND_SESSION_KEY, HASH_SESSION_KEY
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from users.services import UserService


# Create your views here.
def login_view(request):
    if request.method == "GET":
        return render(request, "login.html", {'username': 'admin', 'password': 'admin'})
    elif request.method == "POST":
        username, password = request.POST['username'], request.POST['password']
        if username == 'admin' and password == 'admin':
            if not request.session.session_key:
                request.session.create()
            user_id, created = UserService().create_user(request.session.session_key)
            request.session[SESSION_KEY] = user_id
            request.session[BACKEND_SESSION_KEY] = settings.AUTHENTICATION_BACKENDS[0]
            request.session[HASH_SESSION_KEY] = 'qwerty'
            request.session.modified = True
            return redirect("/")
        else:
            messages.error(request, "Hiss!!! invalid credentials please enter admin, admin")
            return render(request, "login.html", {'username': username, 'password': password})
    return HttpResponse(status=405)


@login_required
def logout_view(request):
    if request.method == "GET":
        if request.session.session_key:
            request.session.delete()
        return redirect("/login")
    return HttpResponse(status=405)
