from django.test import TestCase
from havochome.models import Developer, Device
import requests, json

# Create your tests here.

class DeviceCase(TestCase):
    def testDevice(self):
        device = Device(Codename="oneplus3", Maintainer=Developer(Name="Anushek"), link="https://raw.githubusercontent.com/Arna-Maity/havoc-supported-devices/master/info/oneplus3.json")
        self.assertEqual(device.Codename, "oneplus3")
        self.assertEqual(device.Maintainer.Name, "Anushek")
        self.assertEqual(device.link, "https://raw.githubusercontent.com/Arna-Maity/havoc-supported-devices/master/info/oneplus3.json")

