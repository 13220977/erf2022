

import paho.mqtt.client as mqtt
import warnings


class ShellyMQTT():

    def __init__(self, broker:str = None,
                 topic:str = "shellies/shellyplug-s-<deviceId>/relay/0",
                 user:str = "gustav", token:str = None
                 ) -> None:
        """
        TODO:
            add <deviceId> in default topic value for relay of stwitch status
        """
        self.broker             = broker
        self.topic              = topic
        self.user               = user
        self.token              = token

    def switchMQTT(self, turn:str = None) -> None:
        """
        Connect to Shelly plug-S over MQTT protocol and switch power
        default turn is 'Toggle'
        """

        if not (self.broker and self.topic):
            raise AttributeMissingError("specify broker and topic to connect via MQTT")
        #if not self.token:
        #    warnings.warn("WARNING: if user or token are not set, MQTT verification might not pass")

        client = mqtt.Client(self.user)

        #@client.connect_callback()
        def on_connect(client, userdata, flags, rc):
            print("Connection returned " + str(rc))

        client.on_connect = on_connect

        #@client.connecti_fail_callback()
        def on_connect_fail(client, userdata, flags, rc):
            print("Connection NOT returned ", + str(rc))

        client.on_connect_fail = on_connect_fail

        print(f"broker is {self.broker}")
        client.connect(self.broker)

        if turn is None:    message = "?turn=toggle"
        elif turn == "on":  message = "?turn=on"
        else:               message = "?turn=off"

        @client.publish_callback()
        def on_publish(client, userdata, flags, rc):
            print(f"published message brih @{rc}")

        #client.on_publish = on_publish
        client.publish(self.topic, message)
        return


    def listenMQTT(self):
        client = mqtt.Client(self.user)



def main():
    """
    in AP mode:
        HTTP server on port 80
        IP -> 192.168.33.1/
    announce HTTP service on port 80 via mDNS
        hostname in the form of:
            shelly<model>-XXXXXXXXXXXX
    """
    #connection = ShellyMQTT(broker="mqtt.eclipseprojects.io", topic="TEST", user="gustav")
    #connection.switchMQTT(turn="on")


    mqttBroker ="mqtt.eclipseprojects.io"
    client = mqtt.Client("Temperature_Inside")

    def on_connect():
        print("connection ye")

    client.on_connect = on_connect
    client.connect(mqttBroker)

    def on_publish():
        print("damn, finally a respose")

    client.on_pubish = on_publish
    client.publish("TEMPERATURE", "testing birh")


if __name__ == "__main__":
    main()
