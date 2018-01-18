from mcweb_IP import *

def get_mcweb_IP():
    # Get the public IP for this website and set in config
    i = McwebIP()
    myIP = i.get_public_IP()

