# home-assistant-eet-solmate-mqtt
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

## Quellen
* [Solmate SDK](https://pypi.org/project/solmate-sdk/)
* [Paho MQTT](https://pypi.org/project/paho-mqtt/)