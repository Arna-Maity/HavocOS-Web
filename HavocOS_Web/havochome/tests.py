from django.test import TestCase
from havochome.models import Developer, Device
import requests, json

# Create your tests here.

class DeviceCase(TestCase):
    
    def setUp(self):
        self.device_list = ['I01WD', 'X00T', 'X01BD', 'crosshatch', 'z2_plus', 'potter', 'sanders', 'payton', 'oneplus3', 'bacon', 'hlte', 'raphael', 'dipper', 'davinci', 'tissot', 'chiron', 'sagit', 'beryllium', 'santoni', 'kenzo', 'mido', 'whyred', 'land', 'I001D', 'river', 'violet', 'ocean', 'platina', 'sirius', 'jasmine_sprout', 'laurel_sprout', 'markw', 'vince', 'sakura', 'onclite', 'tulip', 'lavender', 'ysl', 'lucye', 'lithium', 'oneplus2', 'RMX1921']
    
    def testDevice(self):
        device = Device(Codename="oneplus3", Maintainer=Developer(Name="Anushek"), link="https://raw.githubusercontent.com/Arna-Maity/havoc-supported-devices/master/info/oneplus3.json")
        self.assertEqual(device.Codename, "oneplus3")
        self.assertEqual(device.Maintainer.Name, "Anushek")
        self.assertEqual(device.link, "https://raw.githubusercontent.com/Arna-Maity/havoc-supported-devices/master/info/oneplus3.json")

    def testDeviceSpecs(self):
        for device in self.device_list:
            print('Testing Device ',device)
            info_url = "https://raw.githubusercontent.com/Arna-Maity/havoc-supported-devices/master/info/" + device + ".json"
            req = requests.get(info_url).content
            self.assertNotEqual(req,b'')
            info = json.loads(requests.get(info_url).content,encoding='utf-8-sig')
            self.assertIsNotNone(info['codename'])
            self.assertEqual(info['codename'],device)
    