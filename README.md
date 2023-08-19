# Home-Assistant EET Solmate MQTT
MQTT Client für die EET Solmate Photovoltaik mit Speicher.

Der Client schickt alle 5 Minuten alle Solmate Daten an den MQTT-Broker.

Auf den folgenden Topics werden die Daten an den Broker gesendet:
* <code>eet-solmate/status/online</code>
* <code>eet-solmate/timestamp</code>
* <code>eet-solmate/temperature</code>
* <code>eet-solmate/battery_state</code>
* <code>eet-solmate/batter_flow</code>
* <code>eet-solmate/inject_power</code>
* <code>eet-solmate/pv_power</code>
* <code>eet-solmate/mppOutI</code>

## Voraussetzungen
Die folgenden Packages werden benötigt: <code>pip install solmate-sdk paho-mqtt</code>

## Home Assistant Integration
Um die Daten in Home Assistant zu nutzen wird ein MQTT-Broker ([Mosquitto Broker](https://github.com/home-assistant/addons/tree/master/mosquitto)) benötigt.

Danach können Sensoren in die Datei <code>config/configuration.yaml</code> hinzugefügt werden. In der Datei [<code>configuration.yaml</code>](configuration.yaml) ist der Ausschnitt mit Sensoren aufgeführt.

Die Sensoren erscheinen dann als Entitäten und können so genutzt werden.

## Quellen
* [Solmate SDK](https://pypi.org/project/solmate-sdk/)
* [Paho MQTT](https://pypi.org/project/paho-mqtt/)