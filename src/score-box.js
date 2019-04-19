const canvas = document.querySelector('#position-chart')
const ctx = canvas.getContext('2d');
const dim = 250;

const light_grass = '#4e8a4d';
const dark_grass = '#427542';
const sandlot = '#ffc08c';

ctx.fillStyle = light_grass;
ctx.fillRect(0, 0, dim, dim);

function draw_diamond(x, y, size, color){
	ctx.fillStyle = color;
	ctx.moveTo(x, y);
	ctx.beginPath();
	ctx.lineTo(x+size/Math.sqrt(2), y-size/Math.sqrt(2));
	ctx.lineTo(x, y-2*size/Math.sqrt(2));
	ctx.lineTo(x-size/Math.sqrt(2), y-size/Math.sqrt(2));
	ctx.lineTo(x, y);
	ctx.fill();
}

function draw_homeplate(x, y){
	const size = 20;
	ctx.fillStyle = 'white';
	ctx.moveTo(x, y);
	ctx.beginPath();
	ctx.lineTo(x+size/Math.sqrt(2), y-size/Math.sqrt(2));
	ctx.lineTo(x+size/Math.sqrt(2), y-2*size/Math.sqrt(2));
	ctx.lineTo(x-size/Math.sqrt(2), y-2*size/Math.sqrt(2));
	ctx.lineTo(x-size/Math.sqrt(2), y-size/Math.sqrt(2));
	ctx.lineTo(x, y);
	ctx.fill();
}

draw_homeplate(dim/2, dim-50);
