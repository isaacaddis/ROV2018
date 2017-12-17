window.onload = function () {


var tempChart = new CanvasJS.Chart("temperature", {
	animationEnabled: true,
	theme: "light2",
	title:{
		text: "Temperature"
	},
	axisY:{
		includeZero: false
	},
	data: [{        
		type: "line",       
		dataPoints: [
			{ y: 450 },
			{ y: 414},
			{ y: 520, indexLabel: "highest",markerColor: "red", markerType: "triangle" },
			{ y: 460 },
			{ y: 450 },
			{ y: 500 },
			{ y: 480 },
			{ y: 480 },
			{ y: 410 , indexLabel: "lowest",markerColor: "DarkSlateGrey", markerType: "cross" },
			{ y: 500 },
			{ y: 480 },
			{ y: 510 }
		]
	}]
});

var voltageChart = new CanvasJS.Chart("voltage", {
	animationEnabled: true,
	theme: "light2",
	title:{
		text: "Voltage"
	},
	axisY:{
		includeZero: false
	},
	data: [{        
		type: "line",       
		dataPoints: [
			{ y: 450 },
			{ y: 414},
			{ y: 520, indexLabel: "highest",markerColor: "red", markerType: "triangle" },
			{ y: 460 },
			{ y: 450 },
			{ y: 500 },
			{ y: 480 },
			{ y: 480 },
			{ y: 410 , indexLabel: "lowest",markerColor: "DarkSlateGrey", markerType: "cross" },
			{ y: 500 },
			{ y: 480 },
			{ y: 510 }
		]
	}]
});
var depthChart = new CanvasJS.Chart("depth", {
	animationEnabled: true,
	theme: "light2",
	title:{
		text: "Depth"
	},
	axisY:{
		includeZero: false
	},
	data: [{        
		type: "line",       
		dataPoints: [
			{ y: 450 },
			{ y: 414},
			{ y: 520, indexLabel: "highest",markerColor: "red", markerType: "triangle" },
			{ y: 460 },
			{ y: 450 },
			{ y: 500 },
			{ y: 480 },
			{ y: 480 },
			{ y: 410 , indexLabel: "lowest",markerColor: "DarkSlateGrey", markerType: "cross" },
			{ y: 500 },
			{ y: 480 },
			{ y: 510 }
		]
	}]
});
/*
	Temperature
	@author: Isaac Addis (github.com/isaacaddis)
*/
/*
	MAIN FUNCTION
	@param Array (List) from Python program
	
	Guidelines:
		-Index 0 : New Temperature Value
		-Index 1 : New Voltage Value
		-Index 2 : New Depth Value
		
	@todo: HOW TO PUSH A DATAPOINT TO AN OBJECT ?
*/

	function process(arr){
		//temperature
		var obj = {y:int(arr[0])};
		tempChart.data.dataPoints.push(obj);
		//voltage
		//depth
	}
process([1]);
/*
	Render
*/
tempChart.render();
voltageChart.render();
depthChart.render();
}