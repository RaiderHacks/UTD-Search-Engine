import socket, struct

def url2ipv4(hostname):
    return socket.gethostbyname('google.com')

print(url2ipv4('duckduckgo.com'))
