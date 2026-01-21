
from django.contrib.auth.decorators import user_passes_test
from .utils import is_admin, is_staff

def admin_required(view_func):
    return user_passes_test(is_admin)(view_func)

def staff_required(view_func):
    return user_passes_test(
        lambda u: is_admin(u) or is_staff(u)
    )(view_func)