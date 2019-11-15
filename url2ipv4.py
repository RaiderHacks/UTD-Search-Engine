import socket, struct

def url2ipv4(hostname):
    return socket.gethostbyname('google.com')

def ip2long(ip):
    """
    Convert an IP string to long
    """
    packedIP = socket.inet_aton(ip)
    return struct.unpack("!L",packedIP)[0]

ipv4str = url2ipv4('duckduckgo.com')

ipv4long = ip2long(ipv4str)

print("ipv4 address in decimal form: %u" % ipv4long)

print("ipv4 address in binary form: %s" % bin(ipv4long))
