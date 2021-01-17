import subprocess
t_output = str(subprocess.run('/home/pi/IPaddress.sh',capture_output=True,shell=True)
t_output = (t_output.split('stdout=b'))[1]
# print(t_output) #uncomment this if you want to know the index to use (see below) 
IP = (terminaloutput.split())[0] #maybe you'll need to change the index
IP = IP[1:]
