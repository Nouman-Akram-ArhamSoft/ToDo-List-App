from django.urls import path
from . import views

app_name = 'todoapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.log_out, name='log_out'),
    path('register/', views.register, name='register'),
    path('register/successfully_register/', views.successfully_register, name='successfully_register'),
    path('todolist/', views.todo_list, name='todo_list'),
    path('taskdetail/<int:task_id>', views.task_detail, name='task_detail'),
    path('taskdetail/update/<int:task_id>', views.update_task, name='update_task'),
    path('taskdetail/delete/<int:task_id>', views.task_delete, name='task_delete'),
    path('taskdetail/addtask/', views.add_task, name='add_task'),
    path('taskdetail/addtask/add_task_success/', views.insert_success, name='insert_success'),

]
