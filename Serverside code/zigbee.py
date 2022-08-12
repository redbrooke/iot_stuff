import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serial = serial.Serial() 
portList = []

for onePort in ports:
	portList.append(str(onePort))
	print(str(onePort))
	
val = input("Select port: COM")

for x in range(0, len(portList)):
	if portList[x].startswith("COM" + str(val)):
		portVar = "COM" + str(val)
		print(portVar)
		
serial.baudrate = 115200
serial.port = portVar
serial.open()

while True:
	if serial.in_waiting:
		packet = serial.readline()
		processedPacket = packet.decode('utf')
		print(processedPacket)
		#storage = open("output.txt", "a")
		#split = processedPacket.split(":")
		#storage.write('{' + ','.join(split) + '}' + ',' + "\n")
		#storage.close()


