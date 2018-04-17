const shell = require('electron').shell;

function add_new_row(){

	const demo_control = document.createElement('div');
	demo_control.className = "demo-controls";

	const add_btn = document.createElement('button');
	add_btn.className = "demo-button";
	add_btn.innerHTML = 'Add';

	add_btn.onclick = function (){
		const delete_btn = document.createElement('button');
		delete_btn.className = "demo-button";
		delete_btn.innerHTML = "Delete";
		delete_btn.onclick = function (){
			const parent = delete_btn.parentNode;
			parent.parentNode.removeChild(parent);
		}
		add_btn.parentNode.appendChild(delete_btn);
		add_btn.parentNode.removeChild(add_btn);
		add_new_row();
	}

	const input = document.createElement('input');
	input.className = "demo-input";
	input.placeholder = "Enter a command";

	demo_control.appendChild(input);
	demo_control.appendChild(add_btn);
	$('#compounds').append(demo_control);
}

//to display
function add_row(id, cmd){
	const new_demo = document.createElement('div');
	new_demo.className = "demo";

	const new_row = document.createElement('div');
	new_row.id = "compound_id_" + id;
	new_row.className = "demo-wrapper";

	const btn_run = document.createElement("button");
	btn_run.className = 'demo-button';
	btn_run.innerHTML = 'Run';
	btn_run.onclick = function () {
		const child_delete = require('child_process');
		const exec = child_delete.spawn('python', ['forwarding_file.py', cmd]);
		exec.stdout.on('data', (data) => {
            console.log(String.fromCharCode.apply(null, data));
          });
	}

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
		const exec = child_delete.spawn('python', ['save_commands.py', 'dcompound', id]);
		const row = document.getElementById('compound_id_'+id);
		row.parentNode.removeChild(row);
	}

	const input = document.createElement('span');
	input.className = "demo-response";
	input.innerHTML = cmd;

	const btn_update = document.createElement('button');
	btn_update.type = 'submit';
	btn_update.className = "demo-button u-category-green";
	btn_update.innerHTML = "Update";

	demo_control.appendChild(btn_run);
	demo_control.appendChild(input);
	demo_control.appendChild(btn_delete);
	new_row.appendChild(demo_control);
	new_demo.appendChild(new_row);
	$('#compound-section').append(new_demo);
}


//retrieve commands
const child_read = require('child_process');
const exec = child_read.spawn('python', ['save_commands.py', 'rcompound']);
exec.stdout.on('data', (data) => {
	const lines = data.toString().replace(/\r/g, '').split('\n');
	console.log(lines);
	for (let i = 0; i < lines.length-1; i++) {
		var content = lines[i].split('%');
		add_row(content[0].toString(), content[1]);
	}
})

add_new_row();

const new_compound = document.getElementById('new_compound');
new_compound.addEventListener('click', function (event) {
	var commands = document.getElementsByTagName("input");
	var str_commands = '';
	for (var i = 0; i < commands.length; ++i) {
		if (commands[i].value) {
			str_commands = str_commands + commands[i].value + '|';
		}
	}

	if (str_commands){
		const spawn = require('child_process').spawn;
		const scriptExecution = spawn('python', ['save_commands.py', 'ncompound', str_commands]);

		scriptExecution.stdout.on('data', (data) => {
			add_row(data.toString(), str_commands);
		});
	}
	
	const to_delete = document.getElementById('compounds');
	to_delete.innerHTML = "";
	add_new_row();
})

// Xiaoran Xu