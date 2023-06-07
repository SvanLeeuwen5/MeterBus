# boot.py -- run on boot-up
import time
from umqtt.simple import MQTTClient
import ubinascii
import machine
import json

def connect_and_subscribe(client_id, mqtt_config):
    client = MQTTClient(client_id, mqtt_config['host'], mqtt_config['port'], mqtt_config['username'], mqtt_config['password'])
    client.connect()
    return client

def restart_and_reconnect():
    print('Failed to connect to MQTT broker. Reconnecting...')
    time.sleep(2)
    machine.reset()

def main():
    client_id = ubinascii.hexlify(machine.unique_id())
    mqtt_config = json.loads(open('config.json'))['mqtt']

    try:
        client = connect_and_subscribe(client_id, mqtt_config)
    except OSError as e:
        restart_and_reconnect()

    last_message = 0
    message_interval = 5
    counter = 0

    #MBUS = class
    
    while True:
        try:
            client.check_msg()
            if (time.time() - last_message) > message_interval:
                msg = b'Hello #%d' % counter
                client.publish(mqtt_config['topic'], msg)
                last_message = time.time()
                counter += 1
        except OSError as e:
            restart_and_reconnect() 

if __name__ == '__main__':
    main()


