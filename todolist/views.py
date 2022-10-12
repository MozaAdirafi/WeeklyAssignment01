from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.models import TaskItem
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers

@login_required(login_url='/todolist/login/')
def todolist(request):
    data = TaskItem.objects.filter(user = request.user)
    context = {
        'todolist' : data,
        'username' : request.user.username,
        'lastlogin' : request.COOKIES['last_login']      
    }
    return render(request,"todolist.html", context)

@login_required(login_url='/todolist/login/')
def delete_task(request,id):
    task = TaskItem.objects.get(id =id)
    task.delete()
    return redirect('todolist:todolist')

@login_required(login_url='/todolist/login/')
def change_status(request,id):
    status = TaskItem.objects.get(id = id)
    status.is_finished = not(status.is_finished)
    status.save()

    return redirect('todolist:todolist')

@login_required(login_url='/todolist/login/')
# Create your views here.
def create_task(request):
    if request.method == "POST":
        user = request.user
        title = request.POST.get("title")
        description = request.POST.get("description")
        create = TaskItem(user = user,date = datetime.datetime.now(), title = title, description = description )
        create.save()
        return redirect('todolist:todolist')
    return render(request, 'create.html')


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created!')
            return redirect('todolist:login')

    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # login first
            response = HttpResponseRedirect(reverse("todolist:todolist")) # create response
            response.set_cookie('last_login', str(datetime.datetime.now())) # create last_login cookie and add it to response
            return response
        else:
            messages.info(request, 'Wrong Username or Password!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response


@login_required(login_url='/todolist/login/')
def todolist_json(request):
    data_task = TaskItem.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data_task), content_type="application/json")


