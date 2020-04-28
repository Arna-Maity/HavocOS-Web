from django.shortcuts import render
from django.http import HttpResponse
from havochome.models import Developer, Device
import requests, json


def home(request):
    return render(request, 'havochome/home.html')

def about(request):
    l = []
    for i in range(len(Developer.objects.all())): 
        l.append(Developer.objects.get(id=(i+1)))     

    context = { 'devs':  l}
    print(context)
    return render(request, 'havochome/about.html',context)


def downloads(request):
    l = []
    for i in range(len(Device.objects.all())): 
        tmp = {}
        dev = json.loads(requests.get(Device.objects.get(id=(i+1)).link).content,encoding='utf-8-sig')
        tmp['vendor'] = dev['vendor']
        tmp['name'] = dev['name']
        tmp['img'] = dev['image']
        tmp['links'] = Device.objects.get(id=(i+1))
        l.append(tmp)  

    context = { 'devices': l}
    return render(request, 'havochome/downloads.html',context)


def device(request,vendor):
    l = []
    for i in range(len(Device.objects.all())): 
        tmp = {}
        dev = json.loads(requests.get(Device.objects.get(id=(i+1)).link).content,encoding='utf-8-sig')
        if dev['vendor_short'] == vendor:
            tmp['vendor'] = dev['vendor']
            tmp['name'] = dev['name']
            tmp['img'] = dev['image']
            tmp['links'] = Device.objects.get(id=(i+1))
            l.append(tmp)  

    context = { 'devices': l}
    return render(request, 'havochome/downloads.html',context)


def downloads_ver(request,a_ver):
    l = []
    for i in range(len(Device.objects.all())): 
        tmp = {}
        dev = json.loads(requests.get(Device.objects.get(id=(i+1)).link).content,encoding='utf-8-sig')
        print(a_ver," ",dev['versions'])
        if a_ver in dev['versions']:
            tmp['vendor'] = dev['vendor']
            tmp['name'] = dev['name']
            tmp['img'] = dev['image']
            tmp['links'] = Device.objects.get(id=(i+1))
            l.append(tmp)  

    context = { 'devices': l}
    page = 'havochome/downloads_' + 'a' + str(a_ver) + '.html'
    return render(request,page,context)