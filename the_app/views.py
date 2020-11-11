from django.shortcuts import render, HttpResponse,redirect
from .models import User
from django.contrib import messages
from datetime import datetime
import bcrypt
from django.contrib.sessions.models import Session
from wall_app import views as wall_app_views


# Create your views here.
def index(request):
    return render(request, 'index.html')

def login_temp(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        response_from_models = User.objects.validateRegister(request.POST)

        if len(response_from_models) < 1:
            pw_hash = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt()).decode()
            new_user = User(first_name=request.POST['first_name'], last_name=request.POST['last_name'], birthday=request.POST['birthday'] , email=request.POST['email'], password=pw_hash)
            new_user.save()
            id = new_user.id
            request.session['id'] = id
            request.session['name'] = request.POST['first_name']
            request.session['type'] = 'registerd!'
            return redirect('wall_app:wall')
        
        else:
            # send E msgs to C
            for err in response_from_models:
                messages.error(request, err)

    return redirect(index)

def login(request):
    if request.method == 'POST':
        response_from_models = User.objects.validateLogin(request.POST)

        if len(response_from_models) < 1:
            user = User.objects.filter(email=request.POST['email'])
            user_id = user[0].id
            user_name = user[0].first_name
            request.session['id'] = user_id
            request.session['name'] = user_name
            request.session['type'] = 'logged in!'
            #return redirect(loged_in)
            return redirect('wall_app:wall')
        
        else:
            # send E msgs to C
            for err in response_from_models:
                messages.error(request, err)
                
    return redirect('/login_page')


def loged_in(request):
    if request.method == 'GET' and 'id' not in request.session:
        return redirect('wall_app:wall')

    return render(request, 'success.html')


def logout(request):

    request.session.clear()		# clears all keys
    if 'id' in request.session:
        del request.session['id']
    if 'name' in request.session:
        del request.session['name']
    if 'type' in request.session:
        del request.session['type']

    return redirect('the_app:home')
    