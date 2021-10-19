import network,time,dht
from simple import MQTTClient
from machine import I2C,Pin,Timer,TouchPad

# You need to modify the following variables to meet your own situation
ssid = 'ssid'
password = 'password'
Product_ID = '7VJ0IIKQA7'
CLIENT_ID = "7VJ0IIKQA7Light"
user_name = "7VJ0IIKQA7Light;12010126;0CVTE;1670625276"
user_password = '4120fadebe7662b428d6cb45cf6a1878c6e1c079ac7bcfec1deff4c29b6e5df0;hmacsha256'
topic_sub = '7VJ0IIKQA7/Light/data'
topic_pub = '7VJ0IIKQA7/Light/data'

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
        print('WIFI connection successful')
        return True
    else:
        print('WIFI connection fail')
        return False

# MQTT publish
def MQTT_Send(tim):
    # message to be published
    print('Publishing message to {}'.format(topic_pub))
    send_mseg = {
                    "TouchA": TouchA.read()
                 }
    client.publish(topic=topic_pub,
                   msg=str(send_mseg),
                   qos=1,
                   retain=False)

def sub_callback(topic, msg):
    """
    call back function for receiving message from subscription topic
    """
    global client
    print('Received message from subscription topic: {}. message: {}'.format(topic_sub, msg))
    if msg == b'led ON' or msg == b'led on':
        pub_msg = 'LED1: ON-state'
        led.value(1)
    elif msg == b'led OFF' or msg == b'led off':
        pub_msg = 'LED1: OFF-state'
        led.value(0)
    else:
        pub_msg = 'other msg'
    client.publish(topic_pub, pub_msg, retain=True)

if WIFI_Connect(ssid, password):

    TouchA = TouchPad(Pin(4))
    led = Pin(0, Pin.OUT)
    time.sleep(1)

    client = MQTTClient(client_id=CLIENT_ID, server=SERVER, port=PORT, user=user_name, password=user_password, keepalive=60)
    client.set_callback(sub_callback)
    client.connect()
    client.subscribe(topic_sub)
    client.publish(topic_pub, 'ESP32 Device online', retain=True)
    print("Connected to %s, subscribed to %s topic" % (SERVER, topic_sub))

    # Turn on the RTOS timer, publish the message in a 10 seconds period
    tim = Timer(-1)
    tim.init(period=10000, mode=Timer.PERIODIC, callback=MQTT_Send)

    while True:
        client.wait_msg()