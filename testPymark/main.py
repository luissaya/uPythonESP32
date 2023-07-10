# help('modules')
import time
import ubinascii
from umqtt.simple import MQTTClient

# Default MQTT MQTT_BROKER to connect to
MQTT_BROKER = "public.mqtthq.com"
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
TOPIC = b"temperature"
PORT = 1883
# Received messages from subscriptions will be delivered to this callback
def sub_cb(topic, msg):
    print((topic, msg))


def main():
    print("main is runnig")
    mqttClient = MQTTClient(CLIENT_ID, MQTT_BROKER, port=PORT)
    mqttClient.set_callback(sub_cb)
    mqttClient.connect()
    mqttClient.subscribe(TOPIC)
    print("Connected to MQTT  Broker :: {MQTT_BROKER}, and waiting for callback function to be called!")
    while True:
        if True:
            # Blocking wait for message
            mqttClient.wait_msg()
        else:
            # Non-blocking wait for message
            mqttClient.check_msg()
            # Then need to sleep to avoid 100% CPU usage (in a real
            # app other useful actions would be performed instead)
            time.sleep(1)

    mqttClient.disconnect()


if __name__ == "__main__":
    main()