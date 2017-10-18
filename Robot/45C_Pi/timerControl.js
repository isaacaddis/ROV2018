/*
	Underlying logic and control for the timer used on the 2018 Graphical User Interface (GUI) for 45C Robotics
	@author: Isaac Addis (github.com/isaacaddis)
*/
function toggle(state){
	if(state){
		document.getElementById("#play").className = "pause fa fa-pause";
	}
	else if(!state){
		document.getElementById("#play").className = "play fa fa-play";
	}
}
(function($) {

    $(function() {
        var $play  = $('.play'),
            $pause = $('.pause'),
//             $stop  = $('.stop'),
            $time  = $('.time-input'),
            $timer = $('.timer');

        var timer = new Timer({
            onstart : function(millisec) {
		//there are 1000*60 = 60,000 milliseconds in one minute
                var min = Math.round(millisec/60000);
                $timer.text(min);
		toggle(true);
            },
            ontick  : function(millisec) {
                var sec = Math.round(millisec / 1000);
		var minutes = Math.floor(millisec / 60000);
		var seconds = ((millisec % 60000) / 1000).toFixed(0);
		$timer.text(minutes + ":" + (seconds < 10 ? '0' : '') + seconds);
            },
            onpause : function() {
                $timer.text('pause');
		toggle(false);

            },
//             onstop  : function() {
//                 $timer.text('stop');
//             },
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
		while(true){
			toggle();
		}
    });
}(jQuery));

