import subprocess
t_output = str(subprocess.run('/home/pi/IPaddress.sh',capture_output=True,shell=True)
t_output = (t_output.split('stdout=b'))[1]
IP = (terminaloutput.split())[0]
IP = IP[1:]
