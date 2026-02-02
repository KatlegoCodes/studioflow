# accounts/services.py

def sync_user_permissions(user):
    

    if not hasattr(user, 'profile'):
        return

    role = user.profile.role

    if role == 'admin':
        user.is_staff = True
        user.is_superuser = True

    elif role == 'staff':
        user.is_staff = True
        user.is_superuser = False

    else:
        user.is_staff = False
        user.is_superuser = False

    user.save()
