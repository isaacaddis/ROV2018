/*
	@Author Isaac Addis
	@Description The function displaying serial information on the GUI. 
	@Param Data coming in from serial.py. 
*/
function process(msg){
	msg = String(msg);
	if(msg.includes("T1"){
		msg = msg.substring(2,msg.length-1);
		$('#temp').text(msg);
	}
	else if(msg.includes("T2"){
		msg = msg.substring(2,msg.length-1);
		$('#temp2').text(msg);
	}
	else if(msg.includes("V1"){
		msg = msg.substring(2,msg.length-1);
		$('#volt').text(msg);
	}
	else if(msg.includes("V2"){
		msg = msg.substring(2,msg.length-1);
		$('#volt2').text(msg);
	}
}
