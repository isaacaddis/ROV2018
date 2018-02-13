window.onload = function () {

/*
	PROCESS FUNCTION
	@param String containing temp or value from Arduino code
*/
	function process(arr){
		//temperature
		if(arr[0]=="t"){
			arr = arr.slice(1)
			$('#temp').text(String(arr));
		}
		if(arr[0]=="v"){
			arr = arr.slice(1)
			$('#voltage').text(String(arr));
		}
	}
	//todo: timer, update index.html
}