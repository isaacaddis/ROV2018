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

To calibrate the camera for conversion from pixels to meters, find the meter/pixel conversion rate using a basic calibration setup.

In Robot/Vision/, execute the calibration.py script, and align a reference object of **known length** aligned perfectly with the **600x600** screen.

From there, divide known length (in meters, for the MATE competition) by pixel width (600), to find the corresponding conversion rate to the camera.

## OBS

To run (capture mic input and generate predictions. When a satisfactory "vehicle" prediction is given, send command to open claw through Serial):

`
    cd Robot/OBS

    sudo python3 capture.py
`

To complete the OBS task for this year, we chose to use the Google AudioSet dataset for providing labeled urban data that we reasoned could be used to detect the frequency selective acoustive release mechanism during our mission runs.

As for the electronics. a Raspberry Pi is used to interface with a Arduino to open a claw when a confident prediction is given that beeping is detected. (Using the Serial module on both devices)

Make sure to have Tensorflow installed. For compiling the source code onto the Raspberry Pi, CPU-only Tensorflow is used, but in the future a GPU-enabled Tensorflow edition may be used to speed up training times.

