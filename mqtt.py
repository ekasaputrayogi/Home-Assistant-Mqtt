import paho.mqtt.client as mqttclient
import time
import lifxlan

Connected = False
broker_adress = "broker.emqx.io"
port = 1883
user = ""
password = ""
li = []
lifx_bedroom = ""

def on_connect(client, usedata,flags,rc):
    if rc==0:
        print("Client is connected")
        global Connected
        Connected = True
        client.subscribe("LIFX/BEDROOM")
        client.subscribe("LIFX/LIVINGROOM")
    else:
        print("Connection Failed")
def on_message(client, userdata, msg):
    global lifx_bedroom
    if msg.topic == "LIFX/BEDROOM":
        #print(str(msg.payload))
        msg.payload = msg.payload.decode("utf-8") 
        lifx_bedroom = str(msg.payload)
        if lifx_bedroom == "1":
            #lifxlan.light.RED
            print("Red")
        if lifx_bedroom == "Green":
            lifxlan.light.GREEN
            print("Green")
        if lifx_bedroom == "Blue":
            lifxlan.light.BLUE
            print("Blue")
        if lifx_bedroom == "Cyan":
            lifxlan.light.CYAN  
            print("Cyan")  
        
    
        #blink.mains()
        print(lifx_bedroom)
    if msg.topic == "LIFX/LIVINGROOM":
    
        #print(str(msg.payload))
        #lifx_bedroom = msg.payload
        #blink.mains()
        print(lifx_bedroom)
client = mqttclient.Client()
client.username_pw_set(user,password=password)
client.on_message = on_message
client.on_connect=on_connect
client.connect(broker_adress,port=port)
client.loop_start()
time.sleep(1)


def main():
    while True:
        try:
            client.publish("lifx",data)
            print (data)
            #time.sleep(1)
        except:
            pass

main()
