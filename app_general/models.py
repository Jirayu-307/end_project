from django.db import models

# Create your models here.

class Subscription(models.Model):
    STATUS = [
        ('unapproved', 'Unapproved'),
        ('approved', 'Approved'),
        ('banned', 'Banned')
    ]
    
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60, unique=True)
    status = models.CharField(max_length=15, choices=STATUS, default='unapproved')
    registered_at = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey('app_rooms.Room', on_delete=models.SET_NULL, null=True)