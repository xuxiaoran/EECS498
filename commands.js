const shell = require('electron').shell;
//retrieve commands

function add_row(id, cmd){

	const new_demo = document.createElement('div');
	new_demo.className = "demo";

	const new_row = document.createElement('div');
	new_row.id = "row_id_" + id;
	new_row.className = "demo-wrapper";

	const btn_run = document.createElement("button");
	btn_run.type = "submit";
	btn_run.className = 'demo-button';
	btn_run.innerHTML = 'Run';
	btn_run.onclick = function () {
		const child_delete = require('child_process');
		const exec = child_delete.spawn('python', ['forwarding_file.py', cmd]);
		exec.stdout.on('data', (data) => {
            console.log(String.fromCharCode.apply(null, data));
          });
	}

	const temp_div = document.createElement('div');
	temp_div.className = "demo-meta u-avoid-clicks";
	temp_div.innerHTML = "Click to Edit or Delete";

	const demo_box = document.createElement('div');
	demo_box.className = "demo-box";

	const demo_control = document.createElement('div');
	demo_control.className = "demo-controls";

	const btn_delete = document.createElement('button');
	btn_delete.type = 'submit';
	btn_delete.id = id;
	btn_delete.className = 'demo-button u-category-pink';
	btn_delete.innerHTML = 'Delete';

	//delete command
	btn_delete.onclick = function(){
		const child_delete = require('child_process');
		const exec = child_delete.spawn('python', ['save_commands.py', 'delete', id]);
		const row = document.getElementById('row_id_'+id);
		row.parentNode.removeChild(row);
	}

	const input = document.createElement('input');
	input.className = "demo-input";
	input.id = 'update_' + id;
	input.placeholder = cmd;

	const btn_update = document.createElement('button');
	btn_update.type = 'submit';
	btn_update.className = "demo-button u-category-green";
	btn_update.innerHTML = "Update";

	btn_update.onclick = function(){
		var command = document.getElementById('update_' + id).value;
		if (command){
			const child_update = require('child_process').spawn;
			const scriptExecution = child_update('python', ['save_commands.py', 'edit', id, command]);

			scriptExecution.stdout.on('data', (data) => {
				const change_btn = document.getElementById('command_' + id);
				change_btn.innerHTML = command;
				const placehold = document.getElementById('input');
				placehold.placeholder = command;
			});

			var data = JSON.stringify(command);
			scriptExecution.stdin.write(data);
			scriptExecution.stdin.end();
		}
	}

	demo_control.appendChild(btn_run);
	demo_control.appendChild(input);
	demo_control.appendChild(btn_update);
	demo_control.appendChild(btn_delete);
	new_row.appendChild(demo_control);
	new_demo.appendChild(new_row);
	$('#saved-section').append(new_demo);

	const div = document.createElement('div');

	$('#saved-section').append(div);
}

//retrieve commands
const child_read = require('child_process');
const exec = child_read.spawn('python', ['save_commands.py']);
exec.stdout.on('data', (data) => {
	const lines = data.toString().replace(/\r/g, '').split('\n');

	for (let i = 0; i < lines.length-1; i++) {
		var content = lines[i].split('%');
		add_row(content[0].toString(), content[1]);
		console.log(content);
	}
})

// add new command
const new_command = document.getElementById('add');
new_command.addEventListener('click', function (event) {
	var command = document.getElementById("new").value;
	if (command){
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