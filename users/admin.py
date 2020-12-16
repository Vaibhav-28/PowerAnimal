from django.contrib import admin
from .models import Library
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
class LibraryInline(admin.StackedInline):
    model = Library
    can_delete = False
    verbose_name_plural = "library"


class UserAdmin(BaseUserAdmin):
    inlines = (LibraryInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)