# 导入必要的模块
import paho.mqtt.client as mqtt  # 用于操作 MQTT 协议的库
import random  # 用于生成随机数
import time  # 用于控制时间间隔（例如延迟）

# 设置 MQTT 服务器地址
mqtt_broker = "mqtt.eclipse.org"  # 这里使用了免费的公共 MQTT 服务器地址
client = mqtt.Client()  # 创建一个 MQTT 客户端对象，用来与 MQTT 服务器连接和通信

# 连接回调函数：当客户端成功连接到服务器时，自动调用此函数
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")  # 打印连接结果代码，成功连接时会显示 0
    client.subscribe("energyData")  # 订阅主题 "energyData"，接收该主题的数据

# 消息回调函数：当收到消息时，自动调用此函数
def on_message(client, userdata, msg):
    # 打印接收到的消息内容，msg.payload 是消息的内容，decode() 是解码成字符串
    print(f"Received message: {msg.payload.decode()}")

# 将回调函数绑定到客户端
client.on_connect = on_connect  # 连接成功时调用 on_connect 函数
client.on_message = on_message  # 收到消息时调用 on_message 函数

# 连接到 MQTT 服务器，指定服务器地址、端口（默认为 1883）和心跳时间（默认为 60 秒）
client.connect(mqtt_broker, 1883, 60)

# 开始客户端的网络循环，处理连接和接收消息
client.loop_start()

# 发布数据的函数
def publish_data():
    while True:
        # 随机生成电力和热水的消耗数据
        data = f"Electricity: {random.randint(1, 100)} kWh, Hot Water: {random.randint(1, 50)} L"
        # 将生成的数据发布到 "energyData" 主题上
        client.publish("energyData", data)
        print(f"Sent: {data}")  # 打印发送的数据
        time.sleep(5)  # 每隔 5 秒发送一次数据

# 如果脚本是直接运行的，就调用 publish_data 函数开始发布数据
if __name__ == "__main__":
    publish_data()
