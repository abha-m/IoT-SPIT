import serial #serial comm
import time  #to set  delays
import sys 

ser = serial.Serial(port='/dev/ttyS0',baudrate=115200,timeout=2) #connecting the gsm module to the port and setting its baud rate 
print(ser)
ser.write("AT\r") # to check if the connection was successful if yes returns ok
print(ser.read(20)) #dispaly the output of the AT command
ser.write("AT+CSQ\r") 
print(ser.read(20))
ser.write('AT+CMGF=1\r')
print(ser.read(20))

myString = "Hello"
myList = ["8767658591","7738945436","9920067697"]

message = myString
for i in range(len(myList)): # to iterarte through all the numbers
    phoneNumber = myList[i]   #gets the value of the phone number
    print("number = " + phoneNumber + ", message = " + message) 
    time.sleep(5) #delay
    ser.write('''AT+CMGS="''' + phoneNumber + '''"\r''')#establishes a connection to which phone the message has to be sent 
    print(ser.read(20))
    time.sleep(5)
    ser.write(message + "\r")
    time.sleep(5)
    ser.write(chr(26)) #Equivalent to 'ctrl-z' to send the message


#Main function that calls other functions - Makes script reusable
def main():
	pass

	if __name__ == "__main__":
		main()
