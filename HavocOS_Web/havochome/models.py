from django.db import models

class Developer(models.Model):
    Name = models.CharField(max_length=100)
    Role = models.CharField(max_length=100)
    Desc = models.TextField()
    Gitlink = models.CharField(max_length=500)
    Paylink = models.CharField(max_length=500, blank=True)
    Tellink = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.Name


class Device(models.Model):
    Name = models.CharField(max_length=150)
    Codename = models.CharField(max_length=100)
    Maintainer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    Dlink = models.CharField(max_length=500)


    def __str__(self):
        return self.Codename
