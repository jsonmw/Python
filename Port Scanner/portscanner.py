# find open ports in servers, computers, printers

import socket           # create socket objects and gives access to methods
import threading        # emulate multithreading
from queue import Queue # queue FIFO data structure
import sys              # provides access to some variables used or maintained by the interpreter

# definitions
queue = Queue()
open_ports = []
thread_count = 100

start_port = 0
last_port = 1024

# Creates socket object with the given target and port, returning whether
# or not the connection was successful
def portscan(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        return True
    except:
        return False

# Forms a queue of ports for scanning, to allow multiple threads to work
# concurrently
def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

# Handles the logic of calling the portscan function on each port
def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(target, port):
            print("Port {} is open".format(port))
            open_ports.append(port)

# "main method"
if len(sys.argv) != 2:
    print("Usage: python port_scanner.py <target_ip>")
    sys.exit()

target = sys.argv[1]
port_list = range(start_port, last_port)
fill_queue(port_list)

thread_list = []

for t in range(thread_count):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("Open ports are: ", open_ports)


#import socket, import threading, import Queue
# define variables : target IP, a queue to hold ports for threading, a list for returning open ports, max number of threads (for in range(number))
# function to fill queue with the given range of ports
# define the actual port_scan function try socket object(AF_INET, SOCK_STREAM), use .connect(target IP, given port), returns boolean. try/except
# function to handle the overall logic, "while not queue empty" port = "queue.get()", if port_scan(), print "Port {} on IP {} is open" OR have it print the IP address at start

# fill queue
# define thread list as empty
# for t in range(thread_count), return a thread object with target=worker function, add this to the thread list.
# start all threads
# join all threads to exit on completion

# do with this info what you will (import json library?)
# result = {"IP address":target, "Open ports : ": port_list }

## MAKE ANOTHER SCRIPT/PROGRAM THAT FINDS ALL ENDPOINTS ON NETWORK
## AND RUNS THIS SCRIPT ON THEM?