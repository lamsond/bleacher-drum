var lineup_state = [];

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

const lineup_json = document.querySelector('#lineup-json');

function set_lineup(e){
	const border_style = '3px solid black';
	let slot = this.id.charAt(this.id.length-1);
	let player = pitcher_selects[slot-1].value;
	const pos = 'P';
	
	lineup_state.push({slot: slot, player: player, pos: pos});
	console.log(lineup_state);
	lineup_json.value = stringulator(lineup_state);

	this.disabled = true;
	pitcher_selects[slot-1].style.border = border_style;
}

const stringulator = (arr_2d) => {
	let new_arr = [];
	for(let i = 0; i < arr_2d.length; i++){
		new_arr.push(JSON.stringify(arr_2d[i]));
	}
	const lovestring = JSON.stringify(new_arr);
	console.log(lovestring);
	return lovestring;
};

set_buttons.forEach(button => button.addEventListener('click', set_lineup));
