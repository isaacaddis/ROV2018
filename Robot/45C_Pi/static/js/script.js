function smartSystem(mode,val){
	var state = $("#state");
	//Remove any previous styling
	state.removeClass();
	/*
		Temperature sensors 1 and 2
	*/
	if(mode=="T1" || mode=="T2"){
		if(val>0 && val<85){
			state.text("Healthy!");
		}
		else if(val<0 || val>150){
			if(mode=="T1"){
				state.text("Possible Broken Temp1 Sensor!");
			}
			else if(mode=="T2"){
				state.text("Possible Broken Temp2 Sensor!");
			}
			state.addClass("is-danger");
			//todo: panic? system
		}
		else{
			state.text("Critical.");
			state.addClass("is-warning");
			//todo: warning state?
		}
	}
	/*
		12 Volt Sensor
	*/
	if(mode="V1"){
		if(val>17 || val < 5){
			state.addClass("is-danger");
			state.text("Possible Broken 12v Sensor!")
		}
		else{
			state.text("Healthy!");
		}
	}
	/*
		5 Volt Sensor
	*/
	if(mode="V2"){
		if(val> 7 || val<2){
			state.addClass("is-danger");
			state.text("Possible Broken 5v Sensor!")
		}
		else{
			state.text("Healthy!");
		}
	}
}
/*
	@sensor The function displaying serial information on the GUI. 
	@Param Data coming in from serial.py. 
*/
function process(msg){
	msg = String(msg);
	if(msg.includes("T1"){
		msg = msg.substring(2,msg.length-1);
		smartSystem("T1",msg);
		$('#temp').text(msg);
	}
	else if(msg.includes("T2"){
		msg = msg.substring(2,msg.length-1);
		smartSystem("T2",msg);
		$('#temp2').text(msg);
	}
	else if(msg.includes("V1"){
		msg = msg.substring(2,msg.length-1);
		smartSystem("V1",msg);
		$('#volt').text(msg);
	}
	else if(msg.includes("V2"){
		msg = msg.substring(2,msg.length-1);
		smartSystem("V2",msg);
		$('#volt2').text(msg);
	}
}
var timey = new (function() {
    var $countdown,
        $form, // Form used to change the countdown time
        incrementTime = 70,
        currentTime = 30000,
        updateTimer = function() {
            $countdown.html(formatTime(currentTime));
            if (currentTime == 0) {
                Example2.Timer.stop();
                timerComplete();
                Example2.resetCountdown();
                return;
            }
            currentTime -= incrementTime / 10;
            if (currentTime < 0) currentTime = 0;
        },
        timerComplete = function() {
            alert('Example 2: Countdown timer complete!');
        },
        init = function() {
            $countdown = $('#countdown');
            Example2.Timer = $.timer(updateTimer, incrementTime, true);
            $form = $('#example2form');
            $form.bind('submit', function() {
                Example2.resetCountdown();
                return false;
            });
        };
    this.resetCountdown = function() {
        var newTime = parseInt($form.find('input[type=text]').val()) * 100;
        if (newTime > 0) {currentTime = newTime;}
        this.Timer.stop().once();
    };
    $(init);
});
// Add a "checked" symbol when clicking on a list item
var list = document.querySelector('ul');
list.addEventListener('click', function(ev) {
  if (ev.target.tagName === 'LI') {
    ev.target.classList.toggle('checked');
  }
}, false);