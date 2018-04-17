const shell = require('electron').shell;

var keys = document.getElementsByName("key");
for (var i = 0; i < keys.length; ++i) {
  const val = keys[i].value;
  var command = document.getElementById('command');

  keys[i].addEventListener('click', function() {
    console.log(val);
    if (val == 'del') {
      if (command.value != '') {
        command.value = command.value.substring(0, command.value.length-1);
      }
    }
    else if (val == 'space') {
      command.value += ' ';
    }
    else if (val == 'clear') {
      command.value = '';
    }
    else{
      command.value += val;
    }
  })
}

const run_btn = document.getElementById('run');
run_btn.addEventListener('click', function (event) {
  var command = document.getElementById('command');
  const spawn = require('child_process').spawn;
  const scriptExecution = spawn("python", ['forwarding_file.py', command.value]);

  // Handle normal output
  scriptExecution.stdout.on('data', (data) => {
    command.value = '';
  });

  // Write data (remember to send only strings or numbers, otherwhise python wont understand)
  var data = JSON.stringify(command);
  scriptExecution.stdin.write(data);
  // End data write
  scriptExecution.stdin.end();

  command.value = '';
})
