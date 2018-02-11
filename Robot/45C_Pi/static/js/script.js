window.onload = function () {

/*
	Tempature
*/
var tempChart = new CanvasJS.Chart("temperature", {
	animationEnabled: true,
	theme: "light2",
	title:{
		text: "Temperature"
	},
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
	Render
*/
tempChart.render();
voltageChart.render();
depthChart.render();
}
/*
	Stopwatch
*/
(function($) {
    $(function() {
        var $play  = $('.play'),
            $pause = $('.pause'),
            $stop  = $('.stop'),
            $time  = $('.time-input'),
            $timer = $('.timer');

        var timer = new Timer({
            onstart : function(millisec) {
                var sec = Math.round(millisec / 1000);
                $timer.text(sec);
            },
            ontick  : function(millisec) {
                var sec = Math.round(millisec / 1000);
                $timer.text(sec);
            },
            onpause : function() {
                $timer.text('pause');
            },
            onstop  : function() {
                $timer.text('stop');
            },
            onend   : function() {
                $timer.text('end');
            }
        });
        $play.on('click', function() {
			timer.start(15*60);
        });


        $pause.on('click', function() {
            if (timer.getStatus() === 'started') {
                timer.pause();
            }
        });

        $stop.on('click', function() {
            if (/started|paused/.test(timer.getStatus())) {
                timer.stop();
            }
        });


    });
}(jQuery));
