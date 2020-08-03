import os
import sys
instances = sys.argv[1]
port = 34500

i =0
print(instances)
file1 = open("activePorts.txt","w")# create file
file1.close() 
# Append-adds at last 
file1 = open("activePorts.txt","a")#append mode

for i in range(0,int(instances,10)):
	# generates appium instances
	os.system("start /B start cmd.exe @cmd /k appium -a 127.0.0.1 -p "+str(port)+" -bp "+str(port+1)+" --selendroid-port "+str(port+2))
	file1.write(str(port)+"!\n")
	port = port + 3
file1.close()
