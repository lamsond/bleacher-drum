
const pitcher_selects = document.querySelectorAll('.play-select');
pitcher_selects.forEach((pitcher, i) => {
		pitcher.style.display = i == 0 ? 'inline':'none';
});

const set_buttons = document.querySelectorAll('.set-btn');
set_buttons.forEach((button, i) => {
	button.style.display = i == 0 ? 'inline':'none';
	button.addEventListener('click', show_next);
});

function show_next(e){
	let n = this.id.charAt(this.id.length-1);
	console.log(n);
	pitcher_selects[n].style.display = 'inline';
	set_buttons[n].style.display = 'inline';
}
