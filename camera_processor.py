import cv2
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import numpy
import serial 
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portsList = []

for onePort in ports:
    portsList.append(str(onePort))
    print(str(onePort))
    

portVar = None
for x in range(0, len(portsList)):
    if portsList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portVar)
        

if portVar is None:
    print("Selected port is not available.")
    exit()

try:
    serialInst.baudrate = 2400
    serialInst.port = portVar
    serialInst.open()
except Exception as e:
    print(f"Error opening serial port: {e}")
    exit()


def update_frames():

    ret, frame = cap.read()
    if ret:
       
        frame1= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img1 = Image.fromarray(frame1)
        imgtk1 = ImageTk.PhotoImage(image=img1)

       
        lbl_img.imgtk = imgtk1
        lbl_img.configure(image=imgtk1)

       
        
        frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        height, width = frame2.shape[:2]
        
        new_height, new_width = (height // 150, width // 150)

        frame2 = cv2.resize(frame2, 
                           (new_width, new_height),
                           interpolation=cv2.INTER_LINEAR)
        
        print(frame2.flatten())
        
        frame2 = cv2.resize(frame2, 
                           (width, height),
                           interpolation=cv2.INTER_NEAREST)
        
        img2 = Image.fromarray(frame2)
        
        imgtk2 = ImageTk.PhotoImage(image=img2)

      
        grey_img.imgtk2 = imgtk2
        grey_img.configure(image=imgtk2)
    
 
    root.after(10, update_frames)


cap = cv2.VideoCapture(0)

root = tk.Tk()
root.title("Camera Feed")




lbl_img = tk.Label(root)
lbl_img.pack(side = "left")

grey_img = tk.Label(root)
grey_img.pack(side = "right")


update_frames()


root.mainloop()


cap.release()
cv2.destroyAllWindows()
