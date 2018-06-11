# 45C Robotics

This repository features the code for 45C Robotics' entire electronic system in the 2017-18 MATE Robotics Competition. 

For more information about our team, please visit [camsrov.com](http://camsrov.com).

## To run code

**Note**: You must have necessary packages installed for these scripts to run. Make sure you have pip installed and follow error messages.

### Raspberry Pi

`cd ~/Desktop/ROV2018/Robot/45C_Pi && sudo python driver.py`

open another terminal window (Ctrl+Shift+T), and run 

`sudo python ser.py`

### Main control computer

`cd ~/Desktop/ROV2018/Robot/vision && sudo python3 vision.py`

# Developer Information

## Calibration

We've eliminated the need for a calibration step in operating the vision system on the robot!

Simply calculate focal length using the functions in the helper file (in folder Tests/), or calculate these values real time. 

**Note**: You *must* know the real distances from camera
## OBS

To run (capture mic input and generate predictions. When a satisfactory "vehicle" prediction is given, send command to open claw through Serial):

`
    cd Robot/OBS && sudo python3 capture.py
`

To complete the OBS task for this year, we chose to use the Google AudioSet dataset for providing labeled urban data that we reasoned could be used to detect the frequency selective acoustive release mechanism during our mission runs.

As for the electronics. a Raspberry Pi is used to interface with a Arduino to open a claw when a confident prediction is given that beeping is detected. (Using the Serial module on both devices)

Make sure to have Tensorflow installed. For compiling the source code onto the Raspberry Pi, CPU-only Tensorflow is used, but in the future a GPU-enabled Tensorflow edition may be used to speed up training times.

