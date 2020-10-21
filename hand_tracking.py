import cv2
import numpy as np
import glob

# This function records images from the connected camera to specified directory 
# when the "Space" key is pressed.
# directory: should be a string corresponding to the name of an existing 
# directory
def CaptureImages(directory):
    # Open the camera for capture
    # the 0 value should default to the webcam, but you may need to change this
    # for your camera, especially if you are using a camera besides the default
    cam = cv2.VideoCapture(0)
    img_counter = 0
    # Read until user quits
    while True:
        ret, frame = cam.read()
        if not ret:
            break
        # display the current image
        cv2.imshow("Display", frame)
        '''
        def nothing(x):  
            pass  
        cv2.namedWindow("tracks")    
        # Create a Trackbar to choose a value for a parameter    
        cv2.createTrackbar(parameter_value_name, "tracks" , parameter_min_value, parameter_max_value, nothing)  
        '''
        # wait for 1ms or key press
        k = cv2.waitKey(1) #k is the key pressed
        if k == 27 or k==113:  #27, 113 are ascii for escape and q respectively
            #exit
            break
        elif k == 32: #32 is ascii for space
            #record image
            img_name = "captured_image_{}.png".format(img_counter)
            cv2.imwrite(directory+'/'+img_name, frame)
            print("Writing: {}".format(directory+'/'+img_name))
            img_counter += 1
    cam.release()

