from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Customer
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def cutomer_add_togroup(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        Customer.objects.create(
            user=instance,
            name=instance.username,
        )


post_save.connect(cutomer_add_togroup, sender=User)
