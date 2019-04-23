'use-strict'

// get form elements
const month = document.querySelector('#id_date_month');
const day = document.querySelector('#id_date_day');
const year = document.querySelector('#id_date_year');
const away_team = document.querySelector('#id_team_away');
const home_team = document.querySelector('#id_team_home');
 
// get scoreboard elements
const gameday = document.querySelector('.gameday');
const away_team_sb = document.querySelector('#away-team-sb');
const home_team_sb = document.querySelector('#home-team-sb');
 
// event handlers
function updateHomeTeam(e){
	let team = home_team.options[this.selectedIndex].text;
	home_team_sb.innerHTML = team;
}
 
// set up event listeners
home_team.addEventListener('change', updateHomeTeam);

