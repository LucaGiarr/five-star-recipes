from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile
from django.core.exceptions import ObjectDoesNotExist


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(pk=instance.id, user=instance)
        print('Profile created!')


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):

    if created is False:
        instance.profile.save()
        print('Profile saved!')
