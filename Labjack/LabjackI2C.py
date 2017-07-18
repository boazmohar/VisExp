"""
https://labjack.com/support/app-notes/hmc6352-magnetometer-i2c
This short program has been created to interface to the HMC6352 digital compass using a U3 and the I2C protocol.  

The magnetomitor is hooked up to the break out board, thanks sparkfun! and the following ports on the U3 are connected to the break out board:
FIO7 -> SCL
FIO6 -> SDA
GND -> GND
VS -> VCC
"""

#the first step to any python program with labjack's is to import and open the device:
import u3
d = u3.U3()

"""
The next step is to figure out how to communicate to the device using the SPI protocol.
In particular, reading the data sheet and then configuring the labjack to adhere to the requirenments.

datasheet:
A quick reference to what addresses I will be writing to:
the default 7bit slave address is 42(hex) 66 in dec(write) and 43(hex) 67 in dec(read)

the command I will wish to send in order to get info back from the magnetomitor includes the following:
I wish to talk to the address 0x42, and I wish to send one bit, 0x41 (from the HMC6352 interface commands/Responses table, page 5 on the datasheet available on sparkfun's web page)  I also want to receive 2 bytes of information, the MSB and LSB data.  Therefore, I will create the following command in python:

please note that you need to shift the address 0x42 to the right by one bit, 
so send 0x21 instead of 0x42 to the address variable in the I2C function, only applies for our LJpython library.  

d.i2c(0x21,[0x41], NumI2CBytesToReceive = 2)


You can also manually set the AddressByte so that the library communicates to that address and not the default one.  
d.i2c(0x42,[0x41], NumI2CBytesToReceive = 2, AddressByte = 0x42)

"""

#for the sake of being able to read information printed on the command line, I will import the time library to use the function time.sleep() to slow down how often data is requested from the magnetomitor

import time


#this function converts the two bit response of the magnetomitor to an integer
def convert2BytestoInt(bytes):
    i = bytes[0]
    j = bytes[1]
    result = 0
    if(i >=8):
        i = i-8
        result = result+2048
    if(i >=4):
        i = i-4
        result = result + 1024
    if(i >=2):
        i = i-2
        result = result + 512
    if(i>=1):
        i = i-1
        result = result+256
    if(j >=128):
        j = j-128
        result = result + 128
    if(j >= 64):
        j = j-64
        result = result + 64
    if(j >=32):
        j = j-32
        result = result + 32
    if(j >=16):
        j = j-16
        result = result + 16
    if(j >=8):
        j = j-8
        result = result+8
    if(j >=4):
        j = j-4
        result = result + 4
    if(j >=2):
        j =j-2
        result = result + 2
    if(j>=1):
        j = j-1
        result = result+1
    return result

#this infinite loop gets information from the device, converts the results, and prints the results to the command line
while(True):
    response = d.i2c(0x21,[0x41], NumI2CBytesToReceive = 2)
    bytes = response['I2CBytes']
    
    #it is now time to convert the response into a more readable number
    ans = convert2BytestoInt(bytes)
    
    print "degrees: "
    print ans
    time.sleep(.01)




    
    