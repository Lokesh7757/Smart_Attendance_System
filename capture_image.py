import csv
import cv2
import os


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False



import cv2

def takeImages():
    # Open a connection to the camera (0 is the default camera)
    cam = cv2.VideoCapture(0)
    
    # Check if the camera opened successfully
    if not cam.isOpened():
        print("Error: Camera could not be opened.")
        return
    
    # Capture a frame
    ret, frame = cam.read()
    
    if ret:
        # Display the captured frame
        cv2.imshow('Captured Frame', frame)
        cv2.waitKey(0)  # Wait for a key press to close the window
        cv2.destroyAllWindows()
    else:
        print("Error: Could not read a frame.")
    
    # Release the camera
    cam.release()
