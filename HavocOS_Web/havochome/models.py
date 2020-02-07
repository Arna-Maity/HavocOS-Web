from django.db import models

class Developer(models.Model):
    Name = models.CharField(max_length=100)
    Role = models.CharField(max_length=100)
    Desc = models.TextField()
    Gitlink = models.CharField(max_length=500)
    Paylink = models.CharField(max_length=500)
    Tellink = models.CharField(max_length=100)
