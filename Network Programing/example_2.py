"""Modifying example_1.py
In this example i use beautiful soup to extract the text and ignore all html elements of the page
"""

import socket
from bs4 import BeautifulSoup

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('portquiz.net', 80))
cmd = b'GET / HTTP/1.0\r\n'
cmd += b'Host: portquiz.net\r\n'
cmd += b'Accept: text/html\r\n'
cmd += b'\r\n'
my_socket.send(cmd)

response = b''
while True:
    data = my_socket.recv(512)
    if len(data) < 1:
        break
    response += data

my_socket.close()

# Parse the HTML response
soup = BeautifulSoup(response, 'html.parser')

# Extract the text content
content = soup.get_text()

with open ("output", mode='w', encoding='utf-8') as f:
        f.write(content)
print("Output has been stored in Output.txt file.")