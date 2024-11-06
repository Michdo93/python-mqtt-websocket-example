# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt

# Konfiguration des MQTT Brokers
broker = "<broker_ip>"       # IP-Adresse deines MQTT Brokers
port = <broker_port>                  # WebSocket-Port
topic = "#"                  # Abonniertes Thema (z.B. alle Themen)
ws_url = "ws://{}:{}".format(broker, port)

# Callback-Funktion, wenn eine Nachricht empfangen wird
def on_message(client, userdata, msg):
    print("Nachricht erhalten: {} -> {}".format(msg.topic, msg.payload.decode()))

# Callback-Funktion, wenn die Verbindung zum Broker erfolgreich hergestellt wird
def on_connect(client, userdata, flags, rc):
    print("Verbunden mit Broker: {}".format(rc))
    print("Abonniere Thema: {}".format(topic))
    client.subscribe(topic)  # Abonniere das gewünschte Thema

# MQTT-Client erstellen
client = mqtt.Client(transport="websockets")  # Wichtig: WebSockets aktivieren

# Callback-Funktionen registrieren
client.on_connect = on_connect
client.on_message = on_message

# Verbinde zum Broker über WebSocket
client.connect(broker, port, 60)

# Warte auf Nachrichten
client.loop_forever()
