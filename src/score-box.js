'use-strict'

const canvas = document.querySelector('#position-chart')
const ctx = canvas.getContext('2d');
const dim = 250;
const w = 300;
const base_dist = 100;
const inf_sf = 1.5;

const light_grass = '#4e8a4d';
const dark_grass = '#427542';
const sandlot = '#ffc08c';

const points = [
	[w/2, dim-20],
	[w/2 + inf_sf*base_dist/Math.sqrt(2), dim-20 - inf_sf*base_dist/Math.sqrt(2)],
	[w/2 - inf_sf*base_dist/Math.sqrt(2), dim-20 - inf_sf*base_dist/Math.sqrt(2)]
];

ctx.fillStyle = light_grass;
ctx.fillRect(0, 0, w, dim);

function draw_circle(x, y, rad, color){
	ctx.fillStyle = color;
	ctx.beginPath();
	ctx.arc(x, y,rad, 0, 2*Math.PI, true);
	ctx.fill();
}

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
	const size = 8;
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

function draw_infield(){
	ctx.fillStyle = sandlot;
	ctx.beginPath();
	ctx.arc(w/2, dim-19, inf_sf*base_dist, -Math.PI/4, -3*Math.PI/4, true);
	ctx.fill();
	ctx.beginPath();
	ctx.moveTo(points[0][0], points[0][1]);
	ctx.lineTo(points[1][0], points[1][1]);
	ctx.lineTo(points[2][0], points[2][1]);
	ctx.lineTo(points[0][0], points[0][1]);
	ctx.fill();
}

draw_infield();
draw_diamond(w/2, dim-20, base_dist, sandlot);
draw_diamond(w/2, dim-30, base_dist-15, light_grass);
draw_circle(w/2, dim-25, 18, sandlot);
draw_homeplate(w/2, dim-18);



