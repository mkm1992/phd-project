var model = [];
var message = {}
var isOpen = false;
var colors123 = [];
var counter = new Array(7);
var hslL = [];
counter =[0,0,0,0,0,0,0]
var meanL = new Array(7);
meanL =[0,0,0,0,0,0,0]
var changColorCounter = 0;
var colorlen = 0;
//var thresh = 33;
function sendToServer() {
	let imageUrl = document.getElementById("txt_url").value;
	let flag =  document.getElementById("flag").value;
	//let thresh =  document.getElementById("thresh").value;
	//hslL = [];
	changColorCounter = 0;
	let _socket = new socket(imageUrl, flag, getResponse);
	_socket.connected(function() {
		_socket.send()

	})
	
}




function getResponse(msg) {

	//debugger;
	colors123 = [];
	if (msg && msg.data) {
		changColorCounter = 0;
		meanL =[0,0,0,0,0,0,0]
		counter =[0,0,0,0,0,0,0]
		console.log(JSON.parse(msg.data),'++++++++data',msg.data,'------------',JSON.parse(msg.data).model_1d, "this is data given from server");
		let imageUrl = document.getElementById("txt_url").value;
		message = JSON.parse(msg.data);
		hslL = new Array(message.shape[0]*message.shape[1]);
		getImage(imageUrl,JSON.parse(msg.data).model_1d)
		var colors = JSON.parse(msg.data).colors;
		var elem = document.getElementById('color_list');
		var frag = document.createDocumentFragment();
		let flag =  document.getElementById("flag").value;
		elem.innerHTML = ''; 
		colorlen = colors.length;
		for(var i = 0; i < colors.length; i++) {
			console.log(rgbToHex(colors[i][0], colors[i][1], colors[i][2]))
			var li = document.createElement('li');
			var input = document.createElement('input');
			input.setAttribute("type", "color");
			input.value = rgbToHex(colors[i][2], colors[i][1], colors[i][0]);
			colors123.push(colors[i]) 
			// if (flag == 0){
			// 	input.value = rgbToHex(colors[i][0], colors[i][1], colors[i][2]);
			// 	colors123.push(colors[i]) 
			// }
			
			// if (flag==1 ){
			// 	var col23 = hslToRgb(colors[i][0]/255, colors[i][1]/255, colors[i][2]/255)
			// 	colors123.push(col23) 
			// 	//console.log(col23,"colors : 2 3")
			// 	input.value = rgbToHex(col23.r,col23.g,col23.b);

			// }
			console.log(input.value,"colors 1 2 3")

			
			li.appendChild(input);
			frag.appendChild(li);
		}
		console.log(colors123,"color checking")
		elem.appendChild(frag);
		///////////////////////////////

		///////////////////////////////


	}
}

function openClose(){
            document.getElementById('color_list').style.display = isOpen ? 'none' : 'block';
            isOpen = !isOpen;
        }

function drawCanvas(img, model_1d) {
	let canvas = document.getElementById("canvas");
	let can = canvas.getContext("2d");
	canvas.height = message.shape[0];
	canvas.width = message.shape[1];
	can.drawImage(img, 0, 0, message.shape[1], message.shape[0]);

	model = model_1d;

}

function getImage(url, model_1d) {
	let img = new Image();
	//img.src = "http://107.191.48.225/api/v1/blobImage?url=" + url;
	// img.setAttribute("crossOrigin", "")
	//img.src ='http://144.202.57.98:86/api/v1/blobImage?url='+url+'?'+ new Date().getTime()
	img.src = 'http://144.202.57.98:86/api/v1/blobImage?url='+url //+'?'+ new Date().getTime()
	img.crossOrigin = "Anonymous"
	img.onload = function () {
		drawCanvas(img, model_1d);
	}

}

function getImageData(can, canvas, model_1d, image_orig, shape) {

	console.log(can, "the can")
	let colorValue = document.getElementById("color_value").value;
	let imageData = can.getImageData(0, 0, canvas.width, canvas.height);
	let color_num = document.getElementById("color_number").value;

	console.log(shape[0]*shape[1], "the image len")
	//start
	// var k =0
	// for (var i = 0; i <= shape[0]*shape[1]; i += 3) {

	// 		imageData.data[k] = image_orig[i];
	// 		imageData.data[k + 1] = image_orig[i+1];
	// 		imageData.data[k + 2] = image_orig[i+2];

	// 	k = k+4;
  		
	// }
	//Find MeanLight
	//start 
	var countInd = new Array(7);
	countInd =[0,0,0,0,0,0,0]
	if (changColorCounter == 0){
		console.log("hello Mojdeh")
		var k = 0
		
		for (var i = 0; i <= imageData.data.length; i += 4) {
			var currentHSL = rgbToHsl(imageData.data[i], imageData.data[i + 1], imageData.data[i + 2]);
			meanL[model_1d[k]] += currentHSL.l; 
			countInd[model_1d[k]] += 1;
			k = k+1;
	  		
		}
		for (var j=0; j<=colorlen; j++)
		{
			meanL[j] = meanL[j]/countInd[j];

		}
		console.log(meanL,"meanL---------------------------------------------") 

	}

	changColorCounter += 1;


	//end








	//start1
	var rgb = hexToRgb(colorValue);
	console.log(rgb, "the rgb is")
	var hsl = rgbToHsl(rgb.r, rgb.g, rgb.b);
	console.log(hsl, "the hsl is")
	console.log(colors123[0].r,"color checking len")
	var index12 = 1000
	// if (color_num > 0){
	// 	for (var i = 0; i<colors123.length; i++ ){
	// 		if (dist(colors123[i].r, colors123[i].g, colors123[i].b,colors123[color_num-1].r, colors123[color_num-1].g,colors123[color_num-1].b)<thresh && i!= color_num-1)
	// 		{
	// 			index12 = i +1
	// 		}
	// }
	// }


	var k = 0
	for (var i = 0; i <= imageData.data.length; i += 4) {
		if ( model_1d[k] == color_num || model_1d[k] == index12 )
		{

			var currentHSL = rgbToHsl(imageData.data[i], imageData.data[i + 1], imageData.data[i + 2]);
			if (counter[color_num] == 0)
			{
				hslL[k] = currentHSL.l;
			}
			//console.log(meanL,"meanL")
			//console.log(hslL[k],"hslLK")  hsl.l-meanL[color_num] +   //hsl.l-meanL[color_num] + hslL[k]
			var currentRGB = hslToRgb(hsl.h, hsl.s,  hsl.l-meanL[color_num] + hslL[k]);
/////////////////
			// if ( hsl.l<0.05 )
			// {
			// 	var currentRGB = hslToRgb(hsl.h, hsl.s, hslL[k]-0.5);
			// 	//counter[color_num] += 1;
				
			// }
			// if ( hsl.l >0.95 )
			// {
			// 	var currentRGB = hslToRgb(hsl.h, hsl.s, hslL[k]+0.5);
			// 	//counter[color_num] += 1;
				
			// }
///////////////
			// else {
			// 	var currentRGB = hslToRgb(hsl.h, hsl.s, (imageData.data[i + 3]/100)*hsl.l);	
			// }

			

			imageData.data[i] = currentRGB.r;
			imageData.data[i + 1] = currentRGB.g;
			imageData.data[i + 2] = currentRGB.b;
			// if (k<1000)
			// {
			// 	console.log(currentHSL, "the rgb is")
			// }

		}
		k = k+1;
  		
	}
	counter[color_num] += 1;
//end
setTimeout(() => {
	can.putImageData(imageData, 0, 0);

}, 1000)
	// let canvas1 = document.getElementById("canvas1");
	// let can1 = canvas1.getContext("2d");

	// can1.drawImage(imageData, 100, 100, imageData.width, imageData.height);


}


function changeColor() {
	let canvas = document.getElementById("canvas");
	let can = canvas.getContext("2d");

	getImageData(can, canvas, model, message.image_orig, message.shape)

}
