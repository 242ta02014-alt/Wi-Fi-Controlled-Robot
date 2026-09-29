# Wi-Fi Controlled Robot
# ESP32 MicroPython Code

import network
import socket
from machine import Pin

# Motor pins
IN1 = Pin(14, Pin.OUT)
IN2 = Pin(27, Pin.OUT)
IN3 = Pin(26, Pin.OUT)
IN4 = Pin(25, Pin.OUT)

# Create Wi-Fi hotspot
wifi = network.WLAN(network.AP_IF)
wifi.active(True)
wifi.config(essid="Robot", password="12345678")

print("Wi-Fi started")
print("Connect to Wi-Fi: Robot")
print("Password: 12345678")

# Robot functions
def forward():
    IN1.on()
    IN2.off()
    IN3.on()
    IN4.off()

def backward():
    IN1.off()
    IN2.on()
    IN3.off()
    IN4.on()

def left():
    IN1.off()
    IN2.on()
    IN3.on()
    IN4.off()

def right():
    IN1.on()
    IN2.off()
    IN3.off()
    IN4.on()

def stop():
    IN1.off()
    IN2.off()
    IN3.off()
    IN4.off()

# Web page
html = """
<html>
<head>
<title>Robot Control</title>
</head>
<body>
<h1>Wi-Fi Robot</h1>

<a href="/forward"><button>FORWARD</button></a><br><br>
<a href="/left"><button>LEFT</button></a>
<a href="/stop"><button>STOP</button></a>
<a href="/right"><button>RIGHT</button></a><br><br>
<a href="/backward"><button>BACKWARD</button></a>

</body>
</html>
"""

# Start server
server = socket.socket()
server.bind(("0.0.0.0", 80))
server.listen(1)

while True:

    client, address = server.accept()
    request = client.recv(1024)

    request = str(request)

    if "/forward" in request:
        forward()

    elif "/backward" in request:
        backward()

    elif "/left" in request:
        left()

    elif "/right" in request:
        right()

    elif "/stop" in request:
        stop()

    client.send("HTTP/1.1 200 OK\r\n")
    client.send("Content-Type: text/html\r\n\r\n")
    client.send(html)

    client.close()
