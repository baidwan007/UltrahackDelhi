import broadlink
import time

devices=broadlink.discover(timeout=10)
print (devices)
for device in devices:
	device.auth()
	device.set_power(False)

# def switcher(socArray,timeInS,state):
# 	for socket in socArray:
# 		socket.set_power(state)
# 	time.sleep(timeInS)
# 	for socket in socArray:
# 		socket.set_power(not state)

# socArray=[]
# socArray.append(devices[0])
# socArray.append(devices[1])
# switcher(socArray,5,True)
# # time.sleep(5)
# socArray.clear()
# socArray.append(devices[0])
# switcher(socArray,2,True)
# socArray.clear()
# socArray.append(device[2])
# switcher(socArray,5,True)
# socArray.clear()

socArray=[]
socArray.append(devices[0])
socArray.append(devices[1])
timeInS=5
state=True
for socket in socArray:
	socket.set_power(state)
time.sleep(timeInS)
for socket in socArray:
	socket.set_power(not state)

socArray.clear()
socArray.append(devices[0])
timeInS=2
for socket in socArray:
	socket.set_power(state)
time.sleep(timeInS)
for socket in socArray:
	socket.set_power(not state)

socArray.clear()
socArray.append(devices[2])
timeInS=5
for socket in socArray:
	socket.set_power(state)
time.sleep(timeInS)
for socket in socArray:
	socket.set_power(not state)
