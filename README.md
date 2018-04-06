# 45C Robotics

This repository features the code for 45C Robotics' entire electronic system in the 2017-18 MATE Robotics Competition. 

For more information about our team, please visit [camsrov.com](http://camsrov.com).

## To run code

### Raspberry Pi

`cd ~/home/pi/Desktop/ROV2018/Robot/45C_Pi && sudo python driver.py`

open another terminal window (Ctrl+Shift+T), and run 

`sudo python ser.py`

### Main control computer

`cd ~/home/pi/Desktop/ROV2018/Robot/vision && sudo python vision.py`

# Developer Information

## Calibration

To calibrate the camera for conversion from pixels to meters, find the meter/pixel conversion rate using a basic calibration setup.

In Robot/Vision/, execute the calibration.py script, and align a reference object of **known length** aligned perfectly with the **600x600** screen.

From there, divide known length (in meters, for the MATE competition) by pixel width (600), to find the corresponding conversion rate to the camera. 

## Graphical User Interfaces

For this season, we opted to use a graphical user interface (GUI) for pilot operation using the Raspberry Pi 3 using [HTMLPy](http://htmlpy.readthedocs.io/en/master/), and another GUI on the onboard Ubuntu computer using the PyQT4 module. 

To run the operator GUI, change your directory over to /Robot/45C_Pi and run:


```
	$ (sudo) driver.py
```
