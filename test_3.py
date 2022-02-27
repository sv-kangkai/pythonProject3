import socks
import socket
import requests
import time

socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9150)
socket.socket = socks.socksocket

r = requests.get('https://icanhazip.com/')
print(r.content)
time.sleep(999)
