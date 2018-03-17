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
$("#preop_button").click(function(){
	$("#body).html("<!DOCTYPE HTML> 
<html>
   <head>
      <!-- 
         Author: Isaac Addis
         Description: Pre-operation
         -->
      <link rel=\"stylesheet\" href=\"{{ \'css/bulma.min.css\'|staticfile }}\"> 
      <link rel=\"stylesheet\" href=\"{{ \'css/font-awesome.min.css\'|staticfile }}\"> 
      <title>2018 45C Robotics</title>
   </head>
   <body>
      <nav class=\" navbar is-link is-transparent  role navigation\" aria-label=\"main navigation\">
      <div class=\"navbar-brand\">
         <a class=\"navbar-brand navbar-item\" href=\"\">
         45C Robotics
         </a>
         <div class=\"navbar-end\">
            <a class=\"navbar-item\">
            Temp 1: <span id=\"temp\"></span>
            </a>
            <a class=\"navbar-item\">
            Temp 2: <span id=\"temp2\"></span>
            </a>
            <a class=\"navbar-item\">
            Voltage 1: <span id=\"volt\"></span>
            </a>
            <a class=\"navbar-item\">
            Voltage 2: <span id = \"volt2\"></span>
            </a>
            <a id = "back" class=\"navbar-item\">
            GO BACK>
            </a>
         </div>
      </div>
      </nav>
      <section class=\"Aligner \" style = \"height:100vh\">
         <div class=\"\">
            <div class = \"Aligner-item\" id = \"checklist\">
               <p class=\"menu-label\">
                  Pre-Operation Checklist
               </p>
               <ul class=\"menu-list\">
                  <li>
                     <a class=\"is-active\">Building an ocean bottom seismometer (OBS)</a>
                     <ul>
                        <li><a>Cable with connector</a></li>
                        <li><a>Anchor</a></li>
                        <li><a>Release mechanism</a></li>
                     </ul>
                  </li>
               </ul>
            </div>
         </div>
      </section>
      <script src=\"{{ \'js/jquery.min.js\'|staticfile }}\"></script>
      <script src=\"{{ \'js/canvas.min.js\'|staticfile }}\"></script>
      <script src=\"{{ \'js/timer.js\'|staticfile }}\"></script>
      <script src=\"{{ \'js/script.js\'|staticfile }}\"></script> 
   </body>
</html>");
});
$("#op_button").click(function(){
	$("#body).html("<!DOCTYPE HTML> 
<html>
   <!-- 
      Author: Isaac Addis
      Description: For Pilot Operation 
      -->
   <head>
      <link rel=\"stylesheet\" href=\"{{ \'css/bulma.min.css\'|staticfile }}\">
      <link rel=\"stylesheet\" href=\"{{ \'css/font-awesome.min.css\'|staticfile }}\">
      <title>2018 45C Robotics</title>
   </head>
   <body>
      <nav class=\" navbar is-link is-transparent  role navigation\" aria-label=\"main navigation\">
         <div class=\"navbar-brand\">
            <a class=\"navbar-brand navbar-item\" href=\"\">
            45C Robotics
            </a>
            <div class=\"navbar-end\">
               <a class=\"navbar-item\">
               Temp 1: <span id=\"temp\"></span>
               </a>
               <a class=\"navbar-item\">
               Temp 2: <span id=\"temp2\"></span>
               </a>
               <a class=\"navbar-item\">
               Voltage 1: <span id=\"volt\"></span>
               </a>
               <a class=\"navbar-item\">
               Voltage 2: <span id = \"volt2\"></span>
               </a>
               <a class=\"navbar-item\">
               GO BACK>
               </a>
               <a class=\"navbar-item\">
                  Timer: <span id=\"timer\"></span>
                  <span id=\"countdown\">15:00:00</span>
                  <form id=\"example2form\">
                     <input class=\'button is-warning\' type=\'button\' value=\'Play/Pause\' onclick=\'timey.Timer.toggle();\' />
                     <input class=\'button is-danger\' type=\'button\' value=\'Stop/Reset\' onclick=\'timey.resetCountdown();\' />
                     <input type=\'text\' name=\'startTime\' value=\'300\' style=\'width:30px;\' />
                  </form>
               </a>
            </div>
         </div>
      </nav>
      <!-- Non-pilot and Pilots -->
      <div class=\"columns\">
         <div class=\"column\">
            <aside class=\"menu\">
               <p class=\"menu-label\">
                  Non-pilots
               </p>
               <ul class=\"menu-list\">
                  <li>Using flight data to determine the search zone for the wreckage</li>
                  <li>Using tidal data and nautical chart to determine the optimum location for a tidal turbine</li>
                  <li>Determining the optimum location</li>
                  <li>Using tidal current data to calculate the maximum possible megawatt generation at this location</li>
               </ul>
            </aside>
         </div>
         <div class=\"column\">
            <h5 class=\"title is-5\">Pilot Control</h5>
            <li>On board: Grab 2 eelgrass sample with bottom claw</li>
            <li>Underwater: Drop 2 eelgrass samples in the drop off grid</li>
            <li>Underwater: Collect 2 eelgrass samples with bottom claw</li>
            <li>Disconnecting the OBS cable connector from the power and communications hub</li>
            <li>Closing the door of the power and communications hub</li>
            <li>Releasing the OBS from the anchor using A frequency-selective acoustic release</li>
            <li>Move ROV back to pool side while pushing OBS</li>
            <li>Returning the OBS to the side of the pool</li>
            <li>Retrieve ROV from pool</li>
            <li>Collecting two samples of eelgrass for topside analysis</li>
            <li>Attach 1 lift bags to bottom claw and 1 to front claw ROV and submerge back in the pool</li>
            <li>Attach bottom lift bag to debris</li>
            <li>Inflate lift bag / move away from debris area</li>
            <li>Attach front lift bag to engine</li>
            <li>Inflate lift bag</li>
            <li>Move lift bags and engine to pool side and retrieve ROV</li>
         </div>
      </div>
      <script src=\"{{ \'js/jquery.min.js\'|staticfile }}\"></script>
      <script src=\"{{ \'js/canvas.min.js\'|staticfile }}\"></script>
      <script src=\"{{ \'js/timer.js\'|staticfile }}\"></script>
      <script src=\"{{ \'js/script.js\'|staticfile }}\"></script> 
   </body>
</html>");
});
$("#back").click(function(){
	$("#body).html("<!DOCTYPE HTML>
<html>
   <head>
      <link rel=\"stylesheet\" href=\"{{ \'css/bulma.min.css\'|staticfile }}\">
      <link rel=\"stylesheet\" href=\"{{ \'css/font-awesome.min.css\'|staticfile }}\">
      <title>2018 45C Robotics</title>
   </head>
   <body id = \"body\">
      <nav class=\" navbar is-info  role navigation\" aria-label=\"main navigation\">
         <div class=\"navbar-brand\">
            <a class=\"navbar-brand navbar-item\" href=\"\">
            45C Robotics
            </a>
            <div class=\"navbar-end\">
               <a class=\"navbar-item\" style = \"color:white\" >
               Temp 1: <span id=\"temp\"></span>
               </a>
               <a class=\"navbar-item\" style = \"color:white\" >
               Temp 2: <span id=\"temp2\"></span>
               </a>
               <a class=\"navbar-item\" style = \"color:white\">
               Voltage 1: <span id=\"volt\"></span>
               </a>
               <a class=\"navbar-item\" style = \"color:white\">
               Voltage 2: <span id = \"volt2\"></span>
               </a>
               <a class = \"navbar-item\" style = \"color:white\" ><strong>System Status:</strong>
               <span id=\"state\"></span>
               </a>                    
            </div>
         </div>
      </nav>
      <section class=\"Aligner \" style = \"height:100vh\">
         <div class=\"is-grouped\">
            <center>
               <!--
                  <div class = \"Aligner-item\">
                      <p>Welcome.</p>
                  </div>
                  -->
               <br><br>
               <div class=\"row  Aligner-item\">
                  <a class=\" button is-primary is-large is-rounded\" style = \"color:white; text-decoration:none\" id = \"preop_button\">Pre-Operation</a>
               </div>
               <br>
               <div class = \"Aligner-item\">
                  <a class=\" is-rounded button is-large is-warning\" style = \"color:white; text-decoration:none\" id = \"op_button\">Pilot Control</a>
               </div>
            </center>
         </div>
      </section>
      <script src=\"{{ \'js/jquery.min.js\'|staticfile }}\"></script>
      <script src=\"{{ \'js/canvas.min.js\'|staticfile }}\"></script>
      <script src=\"{{ \'js/timer.js\'|staticfile }}\"></script>
      <script src=\"{{ \'js/script.js\'|staticfile }}\"></script> 
   </body>
</html>");
});
