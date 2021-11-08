from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Person(User):

    user_DOB = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Task(models.Model):
    task_title = models.CharField(max_length=100)
    task_type = models.CharField(max_length=100)
    task_description = models.CharField(max_length=200)
    task_start_time = models.DateTimeField(datetime.now(), null=True)
    user = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.task_title} -- {self.task_type}"
