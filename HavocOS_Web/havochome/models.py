from django.db import models
import requests,json

class Developer(models.Model):
    Name = models.CharField(max_length=100)
    Role = models.CharField(max_length=100,null=True)
    Desc = models.TextField()
    Imlink = models.CharField(max_length=500,default="{{ static 'havochome/assets/profile.jpeg' }}")
    Xdalink = models.CharField(max_length=500,blank=True)
    Gitlink = models.CharField(max_length=500, blank=True)
    Paylink = models.CharField(max_length=500, blank=True)
    Tellink = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.Name


class Device(models.Model):
    Codename = models.CharField(max_length=100)
    Maintainer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    link = models.CharField(max_length=500,null=True)
    Xdalink = models.CharField(max_length=500,null=True)
    Sflink = models.CharField(max_length=500,blank=True)


    def __str__(self):
        return self.Codename

    



## Anushek Prasal
#response = requests.get('https://api.github.com/users/skulshady')
#dev = response.json()
#Developer(Name=dev['name'],Role=dev['bio'],Desc='',Imlink=dev['avatar_url'],Xdalink='https://forum.xda-developers.com/member.php?u=7578917',Gitlink=dev['html_url'],Paylink='https://paypal.me/ANUSHEK',Tellink='').save()
#
## Viktor Hermann
#response = requests.get('https://api.github.com/users/zenixxx')
#dev = response.json()
#Developer(Name=dev['name'],Role=dev['bio'],Desc='',Imlink=dev['avatar_url'],Xdalink='https://forum.xda-developers.com/member.php?u=4608158',Gitlink=dev['html_url'],Paylink='https://paypal.me/vhermann ',Tellink='').save()
#
## Arna Maity
#response = requests.get('https://api.github.com/users/arna-maity')
#dev = response.json()
#Developer(Name=dev['name'],Role=dev['bio'],Desc='',Imlink=dev['avatar_url'],Xdalink='',Gitlink=dev['html_url'],Paylink='',Tellink='').save()

