#!/usr/bin/python

# Port-Tester v0.1
# Test which remote ports the server running this script can access to.
# written by localh0t
# Date: 03/02/12
# Contact: mattdch@me.com
# Follow: @mattdch
# localh0t.github.io

import sys,socket,errno

# Functions goes here

def banner():
	return "\n####################\n# Port Tester v0.1 #\n####################"

def exitProgram(code):
	if code==1:
		sys.exit("\n[!] Exiting help...\n")
	if code==2:
		sys.exit("\n[!] Test finished, exiting...\n")
	if code==3:
		sys.exit("\n[!] Exiting...\n")
	if code==4:
		sys.exit("\n[-] Exiting, check arguments...\n")

def strToInt(convert,typeParam):
	try:
		value = int(convert)
		return value
	except:
		print "\n[-] Number given in " + typeParam + " is invalid"
		exitProgram(3)

def checkTimeout(timeout):
	if timeout is None or timeout <= 0:
		# Default timeout : 3 seconds
		timeout = 3
	else:
		pass
	return timeout

def connectHost(host,port,timeout):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(timeout)
		sock.connect((host, port))
		# Connection established, we can access that port
		return "[+] We can reach port " + str(port)
	except:
		# If some error happens (refused / filtered), we cannot access that port, print that
		return "[-] We cannot reach port " + str(port)

if len(sys.argv) <= 4:
	print banner()
	print "\nUsage:\n======\n\npython", sys.argv[0], "-s [START PORT] -e [END PORT] -t [TIMEOUT (Seconds) (Optional, default: 3)]"
	exitProgram(1)

# Set some variables
count = 0
timeout = None
start_port = None
end_port = None

# Read args
for arg in sys.argv:
	if arg == "-s":
		start_port = strToInt(sys.argv[count+1],"-s")
	elif arg == "-e":
		end_port = strToInt(sys.argv[count+1],"-e")
	elif arg == "-t":
		timeout = strToInt(sys.argv[count+1],"-t")
	count+=1

# Do some checks
if start_port is None or end_port is None:
	exitProgram(4)
timeout = checkTimeout(timeout)

# Test started
print banner()
print "\n[!] Port-test started..."
print "[!] Timeout: " + str(timeout) + " seconds\n"

# In case we had DNS problems on the server, we use the IP instead the domain, if you wanna use the domain : hostname = socket.gethostbyname("open.zorinaq.com")
hostname = '163.172.166.150' # open.zorinaq.com , 65k ports open

for port in range(start_port , end_port+1):
	print connectHost(hostname, port, timeout)
exitProgram(2)
