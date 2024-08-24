import cv2
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import numpy as np 
import serial 
import time 

arduino = serial.Serial(port='COM8', baudrate=115200, timeout=.01)

def send_data(num): 
    print(num)
    arduino.write(bytes(num,'utf-8'))
    
    
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
        data = frame2.flatten()
        data = [str(x) for x in data]
        data = "/".join(data)
        send_data(bytes(data,"utf-8"))
        
        
        
        frame2 = cv2.resize(frame2, 
                           (width, height),
                           interpolation=cv2.INTER_NEAREST)
        
        img2 = Image.fromarray(frame2)
        
        imgtk2 = ImageTk.PhotoImage(image=img2)

      
        grey_img.imgtk2 = imgtk2
        grey_img.configure(image=imgtk2)
    
 
    root.after(100, update_frames)


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
