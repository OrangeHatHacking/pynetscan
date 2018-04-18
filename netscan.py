"""
Program created by Matthew Lyons, all credit for ping.py goes to the contributors and creators.
Made as a project, not to replace other network mapping software
"""
import socket,os,re #,threading
from ping import *

soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
soc.connect(("google.com",0))
#get ip
ip = str(socket.gethostbyname(socket.gethostname()))

local_ip = ip

def get_template(ip):
    """
    cuts off end of ip address to get network ip. (regex wouldn't work)
    """
    dot_count = 0
    template = ""
    for i in ip:
        if i==".":
            dot_count+=1
        if dot_count<=2:
            template+=i
    return template

#remove end digits to get network ip template
blank_ip = get_template(local_ip)

def is_loopback(ip):
    """
    Checks if ip passed as an argument is loopback
    """
    if ip == "127.0.0.1" or ip == "127.0.1.1":
        return True
    else:
        return False

#check if local ip is loopback
if is_loopback(local_ip):
    print("Local IP is loopback or out of network IP range!")

def simple_scan(blank_ip):
    """
    sends icmp echo request to all possible devices on network and prints IP address if it is returned
    """
    print("Warning! Will not detect devices set to stealth mode")
    print("Use tcp scan on entire network for more accuracy")
    try:
        #1-254 is range of possible IPs
        for i in range(1,255):
            curr_ip = str(blank_ip+str(i)) #creates current IP to scan
            if is_loopback(curr_ip):
                print("IP is loopback or out of network range!")
            elif verbose_ping(curr_ip): #returns true if IP responds to ping
                print("{} is online".format(curr_ip))
        os.system("clear") #clears screen
    except KeyboardInterrupt:
        print("Stopped by user!")
        main(blank_ip)

def main(blank_ip):
    print("Choose option:")
    print("[1] simple quick scan of entire network")
    print("[2] tcp scan")
    print("[99] Exit")

    opt = int(input(""))

    if opt == 1:
        simple_scan(blank_ip)
    elif opt == 2:
        print("\n_______________________")
        print("not currently available ")
        print("~~~~~~~~~~~~~~~~~~~~~~~\n")
        main(blank_ip)
    elif opt == 99:
        sys.exit(0)
    else:
        print("Invalid input")
        main(blank_ip)

if __name__ == "__main__":
    main(blank_ip)
