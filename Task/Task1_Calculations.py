#-------------------------------------------------------------------------------
# Name:        Task1_Calculations
# Purpose:
#
# Author:      Jiajer Ho
#
# Created:     20/06/2018
#-------------------------------------------------------------------------------


def calculations():
    heading = float(raw_input("Heading (degrees): "))
    ascentAirspeed = float(raw_input("Airspeed ascent (m/s): "))
    timeUntilFailure = float(raw_input("Time Until Engine Failure (seconds): "))
    ascentVector = timeUntilFailure * ascentAirspeed
    print("Ascent Distance: "+ str(ascentVector)+ " meters"+ " at " + str(heading) + " degrees")
    print("On the map, this will be about: "+ str(ascentVector * .7)+ "cm")
    ascentRate = float(raw_input("Ascent Rate (m/s): "))
    height = ascentRate * timeUntilFailure
    descentRate = float(raw_input("Descent Rate (m/s): "))
    descentAirspeed = float(raw_input("Airspeed Descent (m/s): "))
    descentTime = height / descentRate
    descentVector = descentTime * descentAirspeed
    print("Descent Distance: "+ str(descentVector)+ " meters"+ " at " + str(heading) + " degrees")
    print("On the map, this will be about: "+ str(descentVector * .7)+ "cm")
    windPush = float(raw_input("Wind Speed (m/s): ")) * descentTime
    windBlowing = float(raw_input("Wind direction from (degrees): "))-180
    print("Wind Distance: "+ str(windPush)+ " meters"+ " at " + str(windBlowing) + " degrees")
    print("On the map, this will be about: "+ str(windPush * .7)+ "cm")
calculations()
