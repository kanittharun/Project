import paho.mqtt.subscribe as subscribe

CLIENT_ID = '5f7526d2-4571-4afb-9317-829576158ffa'
NETPIE_TOKEN = 'gGXhs95XeBwjjDUyCZzHHS7VGmDNf8xB'

if __name__ == '__main__':
    while True:
        msg = subscribe.simple('@msg/fallevent/#', hostname='mqtt.netpie.io', port=1883, client_id=CLIENT_ID, auth={'username':NETPIE_TOKEN, 'password':None}, keepalive=10)
        msg_str = str(msg.payload)
        print("%s --> %s" % (msg.topic, msg_str))
