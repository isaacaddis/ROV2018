/*
	Underlying logic and control for the timer used on the 2018 Graphical User Interface (GUI) for 45C Robotics
	@author: Isaac Addis (github.com/isaacaddis)
*/
(function($) {
	toggleOn = false;
	function toggle(){
		if(toggleOn){
			document.getElementById("#play").className = "pause fa fa-pause";
		}
		else{
			document.getElementById("#play").className = "play fa fa-play";
		}
	}
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
				toggleOn = true;
            },
            ontick  : function(millisec) {
                var sec = Math.round(millisec / 1000);
                $timer.text(sec);
            },
            onpause : function() {
                $timer.text('pause');
				toggleOn = false;

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
		while(true){
			toggle();
		}
    });
}(jQuery));

