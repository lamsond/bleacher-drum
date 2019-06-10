'use-strict'

// get form elements
const month = document.querySelector('#id_date_month');
const day = document.querySelector('#id_date_day');
const year = document.querySelector('#id_date_year');
const away_team = document.querySelector('#id_team_away');
const home_team = document.querySelector('#id_team_home');
 
// get scoreboard elements
const gameday = document.querySelector('#gameday');
const away_team_sb = document.querySelector('#away-team-sb');
const home_team_sb = document.querySelector('#home-team-sb');
 
// event handlers
function update_home_team(e){
	let team = home_team.options[this.selectedIndex].text;
	home_team_sb.innerHTML = team;
}

function update_away_team(e){
	let team = away_team.options[this.selectedIndex].text;
	away_team_sb.innerHTML = team;
}

function update_date(e){
	const date_str = `${month.value}/${day.value}/${year.value}`;
	gameday.innerHTML = date_str;
}

// set up event listeners
home_team.addEventListener('change', update_home_team);
away_team.addEventListener('change', update_away_team);
month.addEventListener('change', update_date);
//month.addEventListener('load', update_date);
day.addEventListener('change', update_date);
//day.addEventListener('load', update_date);
year.addEventListener('change', update_date);
//year.addEventListener('load', update_date);
window.addEventListener('load', update_date);
