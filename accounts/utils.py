# accounts/utils.py

def is_admin(user):
    if not user.is_authenticated:
        return False
    if not hasattr(user, 'profile'):
        return False
    return user.profile.role == 'admin'

def is_staff(user):
    if not user.is_authenticated:
        return False
    if not hasattr(user, 'profile'):
        return False
    return user.profile.role in ['admin', 'staff']

def get_user_role(user):
    if not user.is_authenticated:
        return 'anonymous'
    if not hasattr(user, 'profile'):
        return 'no-profile'
    return user.profile.role