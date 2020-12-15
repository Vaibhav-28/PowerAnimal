from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Library


@receiver(post_save, sender=User)
def create_library(sender, instance, created, **kwargs):
    if created:
        Library.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_library(sender, instance, **kwargs):
    instance.library.save()