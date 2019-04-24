from umqtt.simple import MQTTClient
import time

def main(server="broker.mqttdashboard.com"):
    c = MQTTClient("umqtt_client", server)
    c.connect()
    while True:
        c.publish(b"something", b"hello")
        time.sleep()

if __name__ == "__main__":
    main()