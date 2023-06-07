# boot.py -- run on boot-up
import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp

def connect_and_subscribe():
    client = MQTTClient(client_id, mqtt_server)
    client.connect()
    return client

def restart_and_reconnect():
    print('Failed to connect to MQTT broker. Reconnecting...')
    time.sleep(10)
    machine.reset()

def main():
    global client_id, mqtt_server
    client_id = ubinascii.hexlify(machine.unique_id())

    try:
        client = connect_and_subscribe()
    except OSError as e:
        restart_and_reconnect()

    mqtt_server = 'REPLACE_WITH_YOUR_MQTT_BROKER_IP'
    topic_pub = b'hello' #TODO
    last_message = 0
    message_interval = 5
    counter = 0

    while True:
        try:
            client.check_msg()
            if (time.time() - last_message) > message_interval:
                msg = b'Hello #%d' % counter
                client.publish(topic_pub, msg)
                last_message = time.time()
                counter += 1
        except OSError as e:
            restart_and_reconnect() 

if __name__ == '__main__':
    main()


