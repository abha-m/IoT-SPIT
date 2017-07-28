import serial
import time
import sys

ser = serial.Serial(port='/dev/ttyS0',baudrate=115200,timeout=2)
print(ser)
ser.write("AT\r")
print(ser.read(20))
ser.write("AT+CSQ\r")
print(ser.read(20))
ser.write('AT+CMGF=1\r')
print(ser.read(20))

myString = "Hello"
myList = ["8767658591","7738945436","9920067697"]

message = myString
for i in range(len(myList)):
    phoneNumber = myList[i]   
    print("number = " + phoneNumber + ", message = " + message)
    time.sleep(5)
    ser.write('''AT+CMGS="''' + phoneNumber + '''"\r''')
    print(ser.read(20))
    time.sleep(5)
    ser.write(message + "\r")
    time.sleep(5)
    ser.write(chr(26))


#Main function that calls other functions - Makes script reusable
def main():
	pass

	if __name__ == "__main__":
		main()
