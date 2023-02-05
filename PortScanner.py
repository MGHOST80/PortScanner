import scapy.all as scapy
import threading
import re
import time
import pyfiglet

#Printing the ASCII art
text=pyfiglet.figlet_format("Mr.Blackhat")
print(text)

def scan_ports(ip):
    #Record start time of scan
    startime = time.time()
    # Loop through ports 1 to 1000
    for port in range(1,1000):
        # Create a packet with the IP and TCP headers
        packet = scapy.IP(dst=ip)/scapy.TCP(dport=port, flags="S")
        # Send the packet and receive a response
        response = scapy.sr1(packet, timeout=1, verbose=0)
        # Check if the response is valid
        if response:
            # Check if the port is open
            if response[scapy.TCP].flags == "SA":
                print("__"* 30)
                print(f'[*]Port {port} is open on {ip}')
    #Record end time of scan
    endtime = time.time()
    print("_" * 30)
    #Calculate the total time taken for the scan
    totaltime = endtime - startime
    print("Scan Completed in ", totaltime)

try:
    # Get user input for the IP address
    IP = input("\n[*]Enter the IP address to scan: ")
except KeyboardInterrupt:
    print("\n[*]Quitting.....")
    exit()

# Validate the user input IP address
ip_valid = re.match("^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", IP)

try:
    if ip_valid:
    # Create a new thread to scan the ports
        thread = threading.Thread(target=scan_ports, args=(IP,))
        thread.start()
        thread.join()
    else:
        print("Invalid IP address")
except KeyboardInterrupt:
    print("\n[*]Quitting.........")
    exit()