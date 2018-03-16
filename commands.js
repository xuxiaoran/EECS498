const shell = require('electron').shell;
//retrieve commands
const commands = document.getElementById('commands');

function add_row(id, cmd){
	const new_row = document.createElement('tr');
	new_row.id = "row_id_" + id;
	const cmd_cell = document.createElement('td');
	const btn_cell = document.createElement('td');
	const btn = document.createElement('button');
	btn.type = 'submit';
	btn.id = id;
	btn.className = 'btn btn-sm btn-danger';
	btn.innerHTML = 'Delete';

	//delete command
	btn.onclick = function(){
		const child_delete = require('child_process');
		const exec = child_delete.spawn('python', ['save_commands.py', 'delete', id]);
		const row = document.getElementById('row_id_'+id);
		row.parentNode.removeChild(row);
	}

	cmd_cell.innerHTML = cmd;
	btn_cell.appendChild(btn);
	new_row.appendChild(cmd_cell);
	new_row.appendChild(btn_cell);
	$('#commands').append(new_row);
}

//retrieve commands
const child_read = require('child_process');
const exec = child_read.spawn('python', ['save_commands.py']);
exec.stdout.on('data', (data) => {
	const lines = data.toString().replace(/\r/g, '').split('\n');

	for (let i = 0; i < lines.length-1; i++) {
		var content = lines[i].split('%');
		add_row(content[0].toString(), content[1]);
	}
})

// add new command
const new_command = document.getElementById('add');
new_command.addEventListener('click', function (event) {
	var command = document.getElementById("new").value;
	if (command != ''){
		const spawn = require('child_process').spawn;
		const scriptExecution = spawn('python', ['save_commands.py', 'add', command]);

		scriptExecution.stdout.on('data', (data) => {
			add_row(data.toString(), command);
			var input = document.getElementById("new");
			input.value = '';
		});

		var data = JSON.stringify(command);
		scriptExecution.stdin.write(data);
		scriptExecution.stdin.end();
	}
})

// Xiaoran Xu
