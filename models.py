from django.db import models

class control(models.Model):
    motor = models.CharField(max_length=2)
    rotate = models.CharField(max_length=9)
    state = models.CharField(max_length=1)
    timestamp = models.DateTimeField(editable=True)
    server_timestamp = models.DateTimeField(editable=True)
