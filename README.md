# 45C Robotics

This repository features the code for 45C Robotics' entire electronic system in the 2017-18 MATE Robotics Competition. 

For more information about our team, please visit [camsrov.com](http://camsrov.com).

## To run code

**Note**: You must have necessary packages installed for these scripts to run. Make sure you have pip installed and follow error messages. We also recommend using *virtualenv* during development. 

### Raspberry Pi

`cd ~/Desktop/ROV2018/Robot/45C_Pi && sudo python driver.py`

This is the main, driver, file that controls the GUI (which is developed in HTML/CSS/JS, but wrapped in Python using htmlPy). Open another terminal window (Ctrl+Shift+T), and run 

`sudo python ser.py`

This is the file that handles getting Arduino sensor input and processing it through Python.

### Main control computer

`cd ~/Desktop/ROV2018/Robot/vision && sudo python3 vision.py`

# Developer Information

## Calibration

We've eliminated the need for a calibration step in operating the vision system on the robot!

Simply calculate focal length using the functions in the helper file (in folder Tests/).

**Note**: To find these values, you **must** have an object of known width and known distance from the camera to work. 

### Vision System

The *Law of Cosines* tells us that given two side lengths and an angle, we can find the missing third side. When the camera is placed in front of two contours, the system of the camera, the first object, and the second object, forms a triangle. Finding the angle measure is relatively straight-forward, for a quick measurement, you can simply place a protractor from the leftmost edge of the camera and measure up to the angle measure the camera marks the protractor.  

![Law of Cosines](https://github.com/isaacaddis/ROV2018/blob/master/Tests/lcos.gif)

## OBS

To run (capture mic input and generate predictions. When a satisfactory "vehicle" prediction is given, send command to open claw through Serial):

`
    cd Robot/OBS && sudo python3 capture.py
`

To complete the OBS task for this year, we chose to use the Google AudioSet dataset for providing labeled urban data that we reasoned could be used to detect the frequency selective acoustive release mechanism during our mission runs.

As for the electronics. a Raspberry Pi is used to interface with a Arduino to open a claw when a confident prediction is given that beeping is detected. (Using the Serial module on both devices)

Make sure to have Tensorflow installed. For compiling the source code onto the Raspberry Pi, CPU-only Tensorflow is used, but in the future a GPU-enabled Tensorflow edition may be used to speed up training times.

If the pre-trained model is needed, please contact me and I will send the models through Google Drive, or a similar service. The models are too large of files to be distributed on Github, and Git LFS never seems to be working the way I want it. 

