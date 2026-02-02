from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance, role="staff")

        if profile.role == "admin":
            instance.is_staff = True
            instance.is_superuser = True
        else:
            instance.is_staff = False

        instance.save()
