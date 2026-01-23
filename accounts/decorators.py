from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .utils import is_admin, is_staff

def admin_required(view_func):
    @login_required
    def wrapper(request, *args, **kwargs):
        if is_admin(request.user):
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, "You need to be an administrator to access this page")
            return redirect("dashboard")
    return wrapper

def staff_required(view_func):
    @login_required
    def wrapper(request, *args, **kwargs):
        if is_admin(request.user) or is_staff(request.user):
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, "You don't have staff permission to access this page")
            return redirect("dashboard")
    return wrapper