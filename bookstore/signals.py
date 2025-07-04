from django.db.models.signals import post_save, post_delete, pre_save, pre_delete
from django.dispatch import receiver
from .models import Books,ISBN

@receiver(pre_save, sender=Books)
def create_isbn(sender, instance, **kwargs):
    print (f"sender:{sender} instnce: {instance}")
    if instance.isbn is None:
        isbn=ISBN.objects.create()
        instance.isbn=isbn
    