var lineup_state = new Array(9);

/* get page elements */
const set_buttons = Array.from(document.querySelectorAll('.set-btn'));
const player_inputs = Array.from(document.querySelectorAll('.play-select'));
const pos_inputs = Array.from(document.querySelectorAll('.pos-select'));
const lineup_json = document.querySelector('#lineup-json');

/* lineup button setup */
function set_lineup(e){
	const border_style = '3px solid black';
	let slot = this.id.charAt(this.id.length-1);
	//console.log(slot);
	let player = player_inputs[slot-1].value;
	//console.log(player);
	let pos = pos_inputs[slot-1].value;
	//console.log(pos);

	lineup_state[slot-1] = {slot: slot, player: player, pos: pos};
	console.log(lineup_state);
	lineup_json.value = lineup_full() ? stringulator(lineup_state):'';
	
	this.disabled = true;
	player_inputs[slot-1].style.border = border_style;
	pos_inputs[slot-1].style.border = border_style;
}
 

const lineup_full = () => {
	for(let i = 0; i < 9; i++){
		if(!lineup_state[i]){
			return false;
		}
	}
	return true;
};

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
