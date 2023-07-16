"""The world’s simplest web browser
simple Python program that makes a connection to a web server and follows the
rules of the HTTP protocol to request a document and display what the server
sends back.
"""
import socket

my_socket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('portquiz.net', 80))

cmd = b'GET http://www.portquiz.net HTTP/1.0\r\n\r\n'

cmd += b'Host: portquiz.net\r\n'
cmd += b'Accept: text/plain\r\n'
cmd += b'\r\n'

my_socket.send(cmd)

while True:
        data = my_socket.recv(512)
        if len(data) < 1:
                break
        print(data.decode('utf-8'), end='')
        
my_socket.close()