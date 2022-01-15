
function sendToServer() {
let url = document.getElementById("txt_url").value;
 var ws =new WebSocket("ws://localhost:8008/cover_rug")
 ws.onmessage = function(msg){
  document.body.innerHTML = "";
  var img = document.createElement('img');
  img.src = "data:image/png;base64, "+ msg.data.slice(0, msg.data.length )
  document.body.appendChild(img)
 }
    ws.onopen=function() {
  ws.send(JSON.stringify({url}))

 } 
}








