from django.db import models

# Create your models here.

class Room(models.Model):
    title = models.CharField(max_length=60)
    price = models.IntegerField()
    is_multiple_bed = models.BooleanField(default=False)
    check_in_date = models.DateTimeField(null=True, blank=True)
    check_out_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)