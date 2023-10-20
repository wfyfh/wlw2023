import paho.mqtt.client as mqtt
import time

HOST = "akpufey.iot.gz.baidubce.com"
PORT = 1883
 
 
def on_message_callback(client, userdata, message):
 
    print(message.topic+" " + ":" + str(message.payload))
    if str(message.payload)=="b'close'":
        client.disconnect()
 
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    #client.subscribe("chanel_01")
 
 
def main():
    client = mqtt.Client('kongzhi001')
    client.username_pw_set('thingidp@akpufey|kongzhi001|0|MD5', 'fb6b96cfb6b85d1d355cc75fe7da51ba')
    client.connect(HOST, PORT, 60)
    client.on_connect = on_connect
    client.publish("AAA", "nihaoa189!!", 1)
    client.subscribe('AAA')
    client.on_message = on_message_callback
    time.sleep(1)
    #client.loop_forever()#如果不需要接受消息此句就不要，但要加延时语句
    

 
 
if __name__ == '__main__':
    main()
 

 