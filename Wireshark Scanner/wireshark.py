import pyshark
import sys
import os.path
import logging

logging.basicConfig(level=logging.ERROR, format='%(asctime)s %(levelname)s %(message)s')

# Get the filename from the command line arguments
filename = sys.argv[1]

# Check that the file exists and is a valid file
if not os.path.isfile(filename):
    logging.error("Invalid file: %s", filename)
    sys.exit(1)

# Create a new capture object from the log file
capture = pyshark.FileCapture(filename)

# Loop through each packet in the capture
for packet in capture:
    
    # Check if the packet contains any HTTP traffic
    if 'HTTP' in packet:
        
        # Print the source and destination IP addresses
        print(packet.ip.src, '->', packet.ip.dst)
        
        # Print the HTTP method and URI
        print(packet.http.request.method, packet.http.request.uri)

# Exit with a success status code
sys.exit(0)

# gonna need to import pyshark

# accept file name as an argument :     import sys, sys.argv[1]
# validate that it's a real file  :     import os.path, 
# use pyshark method to define an object of the capture
# iterate through the cpature looking for particular patterns

# add some particular logging library in the failure exit.