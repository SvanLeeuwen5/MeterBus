# boot.py -- run on boot-up
import network
import esp
import gc

esp.osdebug(None)
gc.collect()

#TODO Replace with your WIFI SSID and PASS
ssid = 'REPLACE_WITH_YOUR_SSID'
password = 'REPLACE_WITH_YOUR_PASSWORD'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')

