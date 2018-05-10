def calculations():
    heading = int(raw_input("Heading: "))
    timeUntilFailure = int(raw_input("Time Until Failure: "))
    airSpeed = int(raw_input("Airspeed (ON ASCENT): "))
    ascentRate = timeUntilFailure * airSpeed
    print("Ascent vector: "+ str(ascentRate)+ " at " + str(heading) + " degrees")
    descentSpeed = int(raw_input("Airspeed (ON DESCENT) rate: "))
    descentRate = descentSpeed * timeUntilFailure
    print("Descent vector: "+ str(descentRate)+ " at " + str(heading) + " degrees")
calculations()






