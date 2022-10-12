# TODO: Implement Routings Here
from django.urls import path
from todolist.views import change_status, create_task, delete_task, register,login_user, logout_user, todolist,todolist_json


app_name = 'todolist'

urlpatterns = [
    path('',todolist, name='todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create_task/', create_task, name='create_task'),
    path('change-status/<int:id>', change_status, name='change_status'),
    path('delete/<int:id>', delete_task, name='delete_task'),
    path('json/', todolist_json, name='todolist_json'),
]
