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
// TODO: Check if this works, may have to do something with the browser or use another approach
var video = document.querySelector('#camera');
navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia || navigator.oGetUserMedia;
 
if (navigator.getUserMedia) {       
    navigator.getUserMedia({video: true}, handleVideo, videoError);
}
 
function handleVideo(stream) {
    video.src = window.URL.createObjectURL(stream);
}
 
function videoError(e) {
    alert("Failure to capture video.")
}
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
		if(arr[0]=="t"){
			arr = arr.slice(1)
			var obj = {y:int(arr[0])};
			tempChart.data.dataPoints.push(obj);
		}
		if(arr[0]=="v"){
			arr = arr.slice(1)
			var obj = {y:int(arr[0])};
			voltageChart.data.dataPoints.push(obj);
		}
	}
/*
	Render
*/
tempChart.render();
voltageChart.render();
depthChart.render();
}