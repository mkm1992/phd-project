let socket = function (imageUrl, flag, getResponse, socketUrl) {
	this.imageUrl = imageUrl;
  this.flag = flag;
  //this.thresh = thresh;
	this.connect(getResponse)
}

socket.prototype.connect = function(getResponse, socketUrl) {
	var socketUrl = socketUrl || "ws:localhost:8008/custom_rug";
	this.socket = new WebSocket(socketUrl);

	this.socket.onmessage = getResponse
}

socket.prototype.send = function () {
	this.socket.send(JSON.stringify({url: this.imageUrl, flag: this.flag}))
}

socket.prototype.connected = function (open) {
	this.socket.onopen = open
}

function rgbToHsl(r, g, b) {
    r /= 255, g /= 255, b /= 255;

    var max = Math.max(r, g, b), min = Math.min(r, g, b);
    var h, s, l = (max + min) / 2;

    if (max == min) {
      h = s = 0; // achromatic
    } else {
      var d = max - min;
      s = l > 0.5 ? d / (2 - max - min) : d / (max + min);

      switch (max) {
        case r:
          h = (g - b) / d + (g < b ? 6 : 0);
          break;
        case g:
          h = (b - r) / d + 2;
          break;
        case b:
          h = (r - g) / d + 4;
          break;
      }

      h /= 6;
    }

    return {h, s, l};
  }

 function hue2rgb(p, q, t) {
    if (t < 0) t += 1;
    if (t > 1) t -= 1;
    if (t < 1 / 6) return p + (q - p) * 6 * t;
    if (t < 1 / 2) return q;
    if (t < 2 / 3) return p + (q - p) * (2 / 3 - t) * 6;
    return p;
  }

 function hslToRgb(h, s, l) {
    var r, g, b;

    if (s == 0) {
      r = g = b = l; // achromatic
    } else {


      var q = l < 0.5 ? l * (1 + s) : l + s - l * s;
      var p = 2 * l - q;

      r = this.hue2rgb(p, q, h + 1 / 3);
      g = this.hue2rgb(p, q, h);
      b = this.hue2rgb(p, q, h - 1 / 3);
    }

    return {r:  Math.floor(r * 255), g:  Math.floor(g * 255), b:  Math.floor(b * 255)};
  }

 function hexToRgb(hex) {
    var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result ? {
      r: parseInt(result[1], 16),
      g: parseInt(result[2], 16),
      b: parseInt(result[3], 16)
    } : null;

  }
function rgbToHex(r, g, b) {
    return "#" + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1);
}

function dist(x1, x2, x3, y1, y2, y3) {

  return Math.sqrt(Math.pow((x1-y1),2)+ Math.pow((x2-y2),2)+ Math.pow((x3-y3),2))
  // body...
}