# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

# from .models import User


# # Register your models here.

# @admin.register(User)
# class TaskManagerUserAdmin(UserAdmin):
#     list_display = ("username", "email", "first_name", "last_name", "is_staff", "verified_email")


from django.contrib import admin
from .models import User
# Register your models here.


admin.site.register(User)