import solmate_sdk
import paho.mqtt.client as mqtt
from time import sleep

solmateSerialnumber = "myserialnumber" #TODO: Durch die Seriennummer der Anlage ersetzen

solmateClient = solmate_sdk.SolMateAPIClient(solmateSerialnumber)
solmateClient.quickstart()

# TODO: Ggf. MQTT Parameter anpassen
mqttBroker = "homeassistant.local"
mqttPort = 1883
mqttClient_id = "solmate-client"
mqttUsername = "mqttuser"
mqttPassword = "mqttpassword"

def mqttConnect():
   def on_connect(client, userdata, flags, rc):
      if(rc == 0):
         print("Connected to MQTT Broker")
      else:
         print("Failed to connect, return code %d\n", rc)
    
   client = mqtt.Client(mqttClient_id)
   client.username_pw_set(mqttUsername, mqttPassword)

   client.on_connect = on_connect
   client.connect(mqttBroker, mqttPort)

   return client

def mqttPublish(mqttClient, topic, data):
   result = mqttClient.publish(topic, data)
    
   status = result[0]
   if(status == 0):
      print(f"Send '{data}' to topic '{topic}'")
   else:
      print(f"Failed to send message to topic {topic}") 

def run():
   mqttClient = mqttConnect()

   try:
      while True:
         liveVals = solmateClient.get_live_values()
         online = solmateClient.check_online()
         mqttPublish(mqttClient, "eet-solmate/status/online", online)

         for property_name in liveVals.keys():
            mqttPublish(mqttClient, f"eet-solmate/{property_name}", liveVals[property_name])

         sleep(60 * 5) # 5 Minuten warten
   except Exception as ex:
      print(ex)

if __name__ == '__main__':
    run()