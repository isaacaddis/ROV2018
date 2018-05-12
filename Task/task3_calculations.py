import math
def calc():
    N = float(raw_input("Number of turbines"))
    p = 1025
    V = float(raw_input("Velocity of the water (in knots)"))*0.514444;
    Cp = float(raw_input("Efficiency of turbines"))
    d = float(raw_input("Diameter of rotor"))
    a = math.pi*((d/2)**2)
    power = N *(.5*(p*a*(V**3)*Cp))*(10**-6)
    print("Expected actual maximum power generation is " + str(power) + "MW")
calc()
