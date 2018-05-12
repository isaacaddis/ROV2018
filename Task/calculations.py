def calculations():
    heading = int(raw_input("Heading: "))
    timeUntilFailure = int(raw_input("Time Until Failure: "))
    airSpeed = int(raw_input("Airspeed (ON ASCENT): "))
    ascentRate = timeUntilFailure * airSpeed
    print("Ascent vector: "+ str(ascentRate)+ " at " + str(heading) + " degrees")
    print("On the map, this will be about: "+ str(ascentRate * .7)+ "cm")
    descentSpeed = int(raw_input("Airspeed (ON DESCENT) rate: "))
    descentRate = descentSpeed * timeUntilFailure
    print("Descent vector: "+ str(descentRate)+ " at " + str(heading) + " degrees")
    print("On the map, this will be about: "+ str(descentRate * .7)+ "cm")
    windPush = int(raw_input("Wind speed")) * timeUntilFailure
    windBlowing = int(raw_input("Wind is blowing from (degrees): "))-180
    print("Wind vector: "+ str(windPush)+ " at " + str(windBlowing) + " degrees")
    print("On the map, this will be about: "+ str(windPush * .7)+ "cm")
calculations()






