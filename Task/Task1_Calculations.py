#-------------------------------------------------------------------------------
# Name:        Task1_Calculations
# Purpose:
#
# Author:      Jiajer Ho
#
# Created:     20/06/2018
#-------------------------------------------------------------------------------


def calculations():
    heading = float(raw_input("Heading: "))
    timeUntilFailure = float(raw_input("Time Until Failure: "))
    ascentAirspeed = float(raw_input("Airspeed (ON ASCENT): "))
    ascentVector = timeUntilFailure * ascentAirspeed
    print("Ascent vector: "+ str(ascentVector)+ " at " + str(heading) + " degrees")
    print("On the map, this will be about: "+ str(ascentVector * .7)+ "cm")
    ascentRate = float(raw_input("Ascent Rate: "))
    height = ascentRate * timeUntilFailure
    decentRate = float(raw_input("Decent Rate: "))
    decentAirspeed = float(raw_input("Airspeed decent: "))
    decentTime = height / decentRate
    descentVector = decentTime * decentAirspeed
    print("Descent vector: "+ str(descentVector)+ " at " + str(heading) + " degrees")
    print("On the map, this will be about: "+ str(descentVector * .7)+ "cm")
    windPush = float(raw_input("Wind speed")) * decentTime
    windBlowing = float(raw_input("Wind is blowing from (degrees): "))-180
    print("Wind vector: "+ str(windPush)+ " at " + str(windBlowing) + " degrees")
    print("On the map, this will be about: "+ str(windPush * .7)+ "cm")
calculations()

