import cv2
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import numpy

# Step 1: Define a function to update the Tkinter window with the camera feed
def update_frames():
    # Capture the latest frame from the camera
    ret, frame = cap.read()
    if ret:
        # Convert the image from OpenCV format (BGR) to PIL format (RGB)
        frame1= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img1 = Image.fromarray(frame1)
        imgtk1 = ImageTk.PhotoImage(image=img1)

        # Update the Tkinter label with the new frame
        lbl_img.imgtk = imgtk1
        lbl_img.configure(image=imgtk1)

         # Convert the image from OpenCV format (BGR) to PIL format (RGB)
        
        frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        height, width = frame2.shape[:2]
        new_height, new_width = (height // 100, width // 100)

        frame2 = cv2.resize(frame2, 
                           (new_width, new_height),
                           interpolation=cv2.INTER_LINEAR)
        
        frame2 = cv2.resize(frame2, 
                           (width, height),
                           interpolation=cv2.INTER_NEAREST)
        
        img2 = Image.fromarray(frame2)
        
        imgtk2 = ImageTk.PhotoImage(image=img2)

        # Update the Tkinter label with the new frame
        grey_img.imgtk2 = imgtk2
        grey_img.configure(image=imgtk2)
    
    # Call this function again after 10ms
    root.after(10, update_frames)


# Step 2: Set up the camera and Tkinter window
cap = cv2.VideoCapture(0)

# Initialize the Tkinter window
root = tk.Tk()
root.title("Camera Feed")



# Create a label to display the camera feed
lbl_img = tk.Label(root)
lbl_img.pack(side = "left")

grey_img = tk.Label(root)
grey_img.pack(side = "right")

# Start updating the Tkinter window with frames from the camera
update_frames()

# Step 3: Run the Tkinter main loop
root.mainloop()

# Step 4: Release the camera when the Tkinter window is closed
cap.release()
cv2.destroyAllWindows()
