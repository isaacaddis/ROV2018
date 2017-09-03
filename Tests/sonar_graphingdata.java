import java.util.Scanner;

/**
 * @author - tedfoodlin
 * 
 * all unnecessary commments are deemed necessary by Joseph Ho 2016
 */

public class sonar_graphingdata 
{
	public static double convertMetersPerSecondToCmPerMicrosecond = 0.0001; //this is the conversion factor from m/s to cm/microsecond
	public static double originalPingSpeed = 0.03508771929 / 2; //this is the ping speed from the sonar sensor (1cm/57microseconds to be exact)
	public static double universalSoundSpeed = 0.0343;
	public static double pingSpeedFactor = originalPingSpeed / universalSoundSpeed;

	public static void main(String[] args) 
	{
		Scanner scan = new Scanner(System.in);
		//try-catch? 
		//.....naaaaahhhh just make sure you dont input wrong stuff
		int index = 0;
//		System.out.println("Input how much test data you got (how many loops happened during test in integer form): ");
//		int i = scan.nextInt();
		int i = 50;
		double factorSum = 0;
		for(index = 0; index < i; index++)
		{
			System.out.println("Input distance from ROV: ");
			double ROVDistance = scan.nextFloat();
			System.out.println("Input temperature from ROV: ");
			double ROVTemperature = scan.nextFloat();
			System.out.println("Input expected distance: ");
			double ExpectedDistance = scan.nextFloat();
			System.out.println("Input expected temperature: ");
			double ExpectedTemperature = scan.nextFloat();
		
			double testedUS = testROVData(ROVDistance, ROVTemperature);
			double expectedUS = testExpectedData(ExpectedDistance, ExpectedTemperature);
			double pingTimeFactor = expectedUS/testedUS;
			System.out.println("Ping Time Factor: " + pingTimeFactor);
			System.out.println(" ");
			factorSum = factorSum + pingTimeFactor;
			
//			System.out.println("Input pingTime");
//			double uS = scan.nextFloat();
////			getExpectedData
//			calculateExpectedData(uS);
		}
//		double pingTimeFactorAvg = factorSum / i;
//		System.out.println("Ping Time Factor Average: " + pingTimeFactorAvg);
		scan.close();
	}
	
	public static double testROVData(double distanceResult, double tempResult)
	{
		double underwaterSoundSpeed = SimplifiedSpeedInWaterEquation(tempResult) * convertMetersPerSecondToCmPerMicrosecond; //this calls the SimplifiedSpeedInWaterEquation (the b and l equation) from a method down below (this is purely for more clarity) and also converts the equation from m/s to cm/microseconds
		double underwaterPingSpeed = pingSpeedFactor * underwaterSoundSpeed; //this might be a place where theres a problem...these don't cancel out correctly
		double uS = distanceResult/underwaterPingSpeed;  // distance = rate * time (with underwater sound speed being temporary all-around solution)
		System.out.println("ping speed from ROV: " + uS + " microseconds");
		return uS;
	}
	public static double testExpectedData(double distanceResult, double tempResult)
	{
		double underwaterSoundSpeed = SimplifiedSpeedInWaterEquation(tempResult) * convertMetersPerSecondToCmPerMicrosecond; //this calls the SimplifiedSpeedInWaterEquation (the b and l equation) from a method down below (this is purely for more clarity) and also converts the equation from m/s to cm/microseconds
		double underwaterPingSpeed = pingSpeedFactor * underwaterSoundSpeed; //this might be a place where theres a problem...these don't cancel out correctly
		double uS = distanceResult/underwaterPingSpeed;  // distance = rate * time (with underwater sound speed being temporary all-around solution)
		System.out.println("expected ping speed: " + uS + " microseconds");
		return uS;
	}
	
	public static void calculateExpectedData(double uS)
	{
		int temperature; //declare variable temperature for testing purposes
		int i = 15; // index for for loop
		//for loop loops through each temperature value from 15 to 35 (degrees celsius) and calculates the adjusted underwater ping speed as well as the final distance for each temperature value 
		for (i = 15; i <= 35; i++){
			temperature = i; //set temperature to the index (so each time it loops thru the temperature changes for the calculations below)
			double underwaterSoundSpeed = SimplifiedSpeedInWaterEquation(temperature) * convertMetersPerSecondToCmPerMicrosecond; //this calls the SimplifiedSpeedInWaterEquation (the b and l equation) from a method down below (this is purely for more clarity) and also converts the equation from m/s to cm/microseconds
			double underwaterPingSpeed = pingSpeedFactor * underwaterSoundSpeed; //this might be a place where theres a problem...these don't cancel out correctly
			double distance = uS * underwaterPingSpeed;  // distance = rate * time (with underwater sound speed being temporary all-around solution)
			
			//prints data to console
			System.out.println("Temperature = " + temperature + " degrees Celsius");
			System.out.println("Distance = " + distance + " cm");
			System.out.println("");
		}
	}
	
	// b and l equation
	public static double SimplifiedSpeedInWaterEquation(double temperature)
	{
		return (1404.3 + 4.7*temperature - (0.04 * Math.pow(temperature, 2)));
	}
	
}

