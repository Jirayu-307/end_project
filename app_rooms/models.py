from django.db import models

# Create your models here.

class Room(models.Model):
    title = models.CharField(max_length=60)
    price = models.IntegerField()
    is_multiple_bed = models.BooleanField(default=False)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    description = models.TextField(null=True)