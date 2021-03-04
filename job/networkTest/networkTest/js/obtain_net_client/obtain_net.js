

function sendToServer() {
	let url = document.getElementById("txt_url").value;
	let type =  document.getElementById("type").value;
	let _socket = new socket(url, type, getResponse);
	_socket.connected(function() {
		_socket.send()

	})
	
}

function getResponse(msg) {

	//debugger;
		console.log(JSON.parse(msg.data),'++++++++data',msg.data,'------------',JSON.parse(msg.data).throughput, "this is data given from server");
		let url = document.getElementById("txt_url").value;
		message = JSON.parse(msg.data);
		let type =  document.getElementById("type").value;
}



