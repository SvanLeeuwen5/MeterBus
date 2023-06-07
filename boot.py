# boot.py -- run on boot-up
import network
import esp
import gc
import json

esp.osdebug(None)
gc.collect()


wifi_config = json.loads(open('config.json'))['wifi']
#TODO Replace with your WIFI SSID and PASS
ssid = wifi_config['SSID']
password = wifi_config['password']

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')

