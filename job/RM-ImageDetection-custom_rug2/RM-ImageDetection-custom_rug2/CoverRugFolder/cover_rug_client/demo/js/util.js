
function sendToServer(url1) {
	console.log(url1, 'sendToServe')
let url = url1;
 var ws =new WebSocket("ws://localhost:8008/cover_rug")
 ws.onmessage = function(msg){
  //document.body.innerHTML = "";
  //var img = document.createElement('img');
  var img = document.getElementsByClassName('img-responsive')[0]
  console.log(img)
  img.src = "data:image/png;base64, "+ msg.data.slice(0, msg.data.length )
  document.body.appendChild(img)
 }
    ws.onopen=function() {
  ws.send(JSON.stringify({url}))

 } 
}



function sendToServer1() {
let url = document.getElementById("txt_url").value;
 var ws =new WebSocket("ws://localhost:8008/cover_rug")
 ws.onmessage = function(msg){
  //document.body.innerHTML = "";
  var img = document.getElementsByClassName('img-responsive')[0]
  console.log(img)
  img.src = "data:image/png;base64, "+ msg.data.slice(0, msg.data.length )
  document.body.appendChild(img)
 }
    ws.onopen=function() {
  ws.send(JSON.stringify({url}))

 } 
}






