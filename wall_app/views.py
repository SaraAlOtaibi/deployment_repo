from django.shortcuts import render, HttpResponse,redirect
from .models import *
from the_app.models import User
from django.contrib import messages
import datetime
import bcrypt
from django.contrib.sessions.models import Session

# Create your views here.
def wall(request):
    context = {
    "messages" : Message.objects.all(),
    }
    return render(request, 'wall.html', context)

def post_msg(request):
    user = User.objects.get(id = request.session['id'])
    msg = Message(message=request.POST['the_msg'], owner=user)
    msg.save()
    return redirect('/wall')

def post_comment(request):
    user = User.objects.get(id = request.session['id'])
    msg = Message.objects.get(id = request.POST['msg_id'])
    comment = Comment(comment=request.POST['comment'], message=msg, owner=user)
    comment.save()
    return redirect('/wall')

def delete_msg(request):
    now = datetime.datetime.now().timestamp()
    msg = Message.objects.get(id=request.POST['msg_id'])
    #msg_date = datetime.datetime.strptime(str(msg.created_at), '%m/%d/%Y %H:%M:%S.%f')
    #msg_date = datetime.datetime.strptime(str(msg.created_at), "%Y-%m-%d")
    #mag_date = datetime.datetime(msg.created_at).timestamp()
    msg_date = msg.created_at.timestamp()
    tdelta = now - msg_date
    minutes = tdelta.total_seconds() / 60
    if(minutes < 30):
        msg.delete()

    return redirect(request, 'wall.html')