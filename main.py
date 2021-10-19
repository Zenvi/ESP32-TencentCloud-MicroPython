import network,time,dht
from simple import MQTTClient
from machine import I2C,Pin,Timer,TouchPad

# You need to modify the following variables to meet your own situation
ssid = 'Input your ssid here'
password = 'Input your wifi password here'
topic = 'V505MLWAFS/TouchPadA/data'
CLIENT_ID = "V505MLWAFSTouchPadA"
user_name = "V505MLWAFSTouchPadA;12010126;QK8XH;1670611788"
user_password = '8d2070ea12718358aa09a2a0adb75f0076853ead6a54e6ccc85d17738f31fb6d;hmacsha256'
Product_ID = 'V505MLWAFS'

SERVER = Product_ID + ".iotcloud.tencentdevices.com"
PORT = 1883

def WIFI_Connect(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    if wlan.isconnected():
        return True
    else:
        return False

# MQTT publish
def MQTT_Send(topic):
    # message to be published
    send_mseg = {
                    "TouchA": TouchA.read()
                 }
    client.publish(topic=topic,
                   msg=str(send_mseg),
                   qos=1,
                   retain=False)


if WIFI_Connect(ssid, password):

    TouchA = TouchPad(Pin(4)) 
    time.sleep(1)

    client = MQTTClient(client_id=CLIENT_ID, server=SERVER, port=PORT, user=user_name, password=user_password, keepalive=60)
    client.connect()

    # Turn on the RTOS timer, publish the message in a 10 seconds period
    tim = Timer(-1)
    tim.init(period=10000, mode=Timer.PERIODIC, callback=MQTT_Send)
