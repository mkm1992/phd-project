let socket = function (url, type, getResponse, socketUrl) {
	this.url = url;
  this.type = type;
  //this.thresh = thresh;
	this.connect(getResponse)
}

socket.prototype.connect = function(getResponse, socketUrl) {
	var socketUrl = socketUrl || "ws:localhost:8008/obtain_net";
	this.socket = new WebSocket(socketUrl);

	this.socket.onmessage = getResponse
}

socket.prototype.send = function () {
	this.socket.send(JSON.stringify({url: this.url, type: this.type}))
}

socket.prototype.connected = function (open) {
	this.socket.onopen = open
}

