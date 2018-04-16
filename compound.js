const shell = require('electron').shell;

function add_row(){
	const new_tr = document.createElement('tr');

	const new_td = document.createElement('td');
	const second_td = document.createElement('td');
	
	const new_cmd = document.createElement('input');
	new_cmd.className = "form-control";

	const add_btn = document.createElement('button');
	add_btn.className = "btn btn-info";
	add_btn.innerHTML = "Add";

	add_btn.onclick = function (){
		add_btn.parentNode.removeChild(add_btn);
		add_row();
	}

	new_td.appendChild(new_cmd);
	second_td.appendChild(add_btn);
	new_tr.appendChild(new_td);
	new_tr.appendChild(second_td);
	$('#commands').append(new_tr);
}

add_row();

const new_compound = document.getElementById('new_compound');
new_compound.addEventListener('click', function (event) {
	var commands = document.getElementsByTagName("input");
	var str_commands = '';
	for (var i = 0; i < commands.length; ++i) {
		if (commands[i].value) {
			console.log(commands[i].value);
			str_commands = str_commands + commands[i].value + '|';
		}
	}

	if (str_commands){
		const spawn = require('child_process').spawn;
		const scriptExecution = spawn('python', ['save_commands.py', 'ncompound', str_commands]);

		scriptExecution.stdout.on('data', (data) => {
			console.log('success');
		});
	}
	window.close();
})
// Xiaoran Xu