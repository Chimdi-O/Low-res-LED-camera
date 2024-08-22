import serial
import time

# Set up the serial connection
arduino = serial.Serial(port='COM11', baudrate=115200, timeout=.01)


while True:
    num = input("Enter a number: ")   # Take input from the user
    arduino.write(bytes(num,'utf-8'))
    print(arduino.readline())
