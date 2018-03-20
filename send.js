
const shell = require('electron').shell;
const exLinksBtn = document.getElementById('run');

exLinksBtn.addEventListener('click', function (event) {
  var command = document.getElementById("command").value;
  const spawn = require('child_process').spawn;
  const scriptExecution = spawn("python", ["main.py"]);

          // Handle normal output
          scriptExecution.stdout.on('data', (data) => {
            console.log(String.fromCharCode.apply(null, data));
          });

          // Write data (remember to send only strings or numbers, otherwhise python wont understand)
          var data = JSON.stringify(command);
          scriptExecution.stdin.write(data);
          // End data write
          scriptExecution.stdin.end();
        })
