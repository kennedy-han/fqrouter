# *Guesser* works with *Scanner* to help establish TCP connection:
# Send SYN out through via Scanner using UDP
# Receive SYN+ACK from remote *Server* (The one Client is making request to)
# Know the external ip and port used by the connection
from . import output

def start():
    output.monitor_output()