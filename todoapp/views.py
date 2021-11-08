from datetime import date
import calendar
from django.shortcuts import render
from .models import Person,  Task
from django.http import  HttpResponse,  HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth import authenticate,  login,  logout
from django.db import IntegrityError

# Create your views here.

def index(request):
    """
        This function is used to render the index page of ToDo app
        :param request:
        :return:
            Render the index page of ToDo app
    """
    return render(request, 'todoapp/index.html')


def register(request):
    """
        This function is used to render the register page of ToDo app
        :param request:
        :return:
            Render the register page of ToDo app
    """
    return render(request, 'todoapp/register.html')


def login_user(request):
    """
        This function is used for validate the user and login it on django admin
        and also used for rendering the login page for ToDo app
        :param request:
        :return:
            Render the Login page of ToDo app
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user == None)
        if user:
            login(request, user)
            return HttpResponseRedirect('/todoapp/todolist/')
        else:
            return HttpResponse('Not valid User')
    else:
        return render(request, 'todoapp/login.html')


def get_current_user(request):
    """
        This Function is used to get the current Person object
        :param request:
        :return:
            Render the Login page of ToDo app
    """
    login_user(request)
    user = request.user
    person = Person.objects.get(username=user)
    return person


def todo_list(request):
    """
        This Function is used to render the specific login person task details
        :param request:
        :return:
            Render the task List page of ToDo app
    """
    person = get_current_user(request)
    todo_list = Task.objects.filter(user=person.user_ptr_id)
    specific_task = []

    for item in todo_list:
        if item.user_id == person.user_ptr_id:
            specific_task.append((item))

    my_date = date.today()
    today = calendar.day_name[my_date.weekday()]

    return render(request, 'todoapp/todolist.html',
                  {'todo_list' : specific_task, 'today' : today,
                   'date' : my_date})



def successfully_register(request):
    """
        This Function is used to register the user in register page
        :param request: str
        :return:
            Render the Successful register page or unsuccessful register page
    """
    first_name = request.POST['firstname']
    last_name = request.POST['lastname']
    user_name = request.POST['username']
    password = request.POST['password']
    date_of_birth = request.POST['dateofbirth']
    email = request.POST['email']

    person_obj = Person(first_name=first_name, last_name=last_name,
                        username=user_name,
                        user_DOB= date_of_birth, email= email)

    person_obj.set_password(password)
    person_obj.is_staff = True

    try:
        person_obj.save()
        return render(request, 'todoapp/register_success.html')
    except IntegrityError:
        return render(request, 'todoapp/not_register.html')


def check_request(request):
    """
        This Function is used to validate the request
        :param request: str
        :return: return the bool value against request condition
    """

    if str(request.user) != 'AnonymousUser':
        return True
    else:
        return False


def task_detail(request, task_id):
    """
        This Function is used to get the specific task details
        :param request: str
        :param task_id: int
        :return: Render the Task Detail page of ToDo app
    """
    if check_request(request):
        task_obj = Task.objects.get(pk=task_id)
        return render(request, 'todoapp/task_detail.html', {'task_obj' : task_obj})
    else:
        return HttpResponseForbidden()


def update_task(request, task_id):
    """
        This Function is used to update the specific task from task detail page
        :param request: str
        :param task_id: int
        :return: render the update success page of Todo App
    """
    task_obj = Task.objects.get(pk=task_id)
    task_obj.task_title = request.POST['tasktitle']
    task_obj.task_type = request.POST['tasktype']
    task_obj.task_description = request.POST['taskdescription']

    task_obj.save()

    return render(request, 'todoapp/update success.html')


def add_task(request):
    """
        This function is used to render the add task page of Todo app
        :param request: str
        :return: Render the add task page
    """
    if check_request(request):
        return render(request, 'todoapp/add_task.html')
    else:
        return HttpResponseForbidden()


def insert_success(request):
    """
        This function is used to insert the task on todolist page
        :param request: str
        :return: render the successfully add task page
    """
    person = request.user
    person_obj = Person.objects.get(username = person)
    task_title = request.POST['tasktitle']
    task_type = request.POST['tasktype']
    task_description = request.POST['taskdescription']


    task_obj = Task(task_title=task_title, task_type=task_type, task_description=task_description, user=person_obj)
    task_obj.save()
    return render(request, 'todoapp/add_task_success.html')


def task_delete(request, task_id):
    """
        This Function is used to delete the task from task detail page
        :param request: str
        :param task_id: int
        :return: render the task delete page of ToDo app
    """
    if check_request(request):
        task_obj = Task.objects.get(id = task_id)
        task_obj.delete()
        return render(request, 'todoapp/task_delete.html')

    else:
        return HttpResponseForbidden()


def log_out(request):
    """
        This Function is used to Log out the user
        :param request: str
        :return: Http response of successfully logout massage
    """
    logout(request)
    return render(request, "todoapp/index.html")