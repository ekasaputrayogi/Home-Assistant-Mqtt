import paho.mqtt.client as mqttclient
import time

Connected = False
broker_adress = "151.106.113.229"
port = 1883
user = "greekindo"
password = "@greekindo123"
li = []
ReceiveData = ""


def on_connect(client, usedata,flags,rc):
    if rc==0:
        print("Client is connected")
        global Connected
        Connected = True
        client.subscribe("office/rgb1/light/switch")
    else:
        print("Connection Failed")
def on_message(client, userdata, msg):
    global ReceiveData
    print(str(msg.payload))
    ReceiveData = msg.payload


client = mqttclient.Client()
client.username_pw_set(user,password=password)
client.on_message = on_message
client.on_connect=on_connect
client.connect(broker_adress,port=port)
client.loop_start()
time.sleep(1)


def main():
    while True:
        client.publish("IOTBOX",data)
        print (data)
        #time.sleep(1)
    except:
        pass

main()
