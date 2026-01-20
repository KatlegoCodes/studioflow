
def is_admin(user):
    return hasattr(user, 'profile') and user.profile.role == 'admin'

def is_staff(user):
    return hasattr(user, 'profile') and user.profile.role == 'staff'