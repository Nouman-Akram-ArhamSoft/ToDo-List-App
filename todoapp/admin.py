from django.contrib import admin
from .models import Person, Task

class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'username', 'password', 'user_DOB', 'email']

    fieldsets = (
        ('Information', {'fields' : ('first_name', 'last_name', 'username', 'password', 'user_DOB', 'email')}),
    )

# Register your models here.
admin.site.register(Person, PersonAdmin)
admin.site.register(Task)