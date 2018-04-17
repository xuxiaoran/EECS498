const shell = require('electron').shell;
const new_command = document.getElementById('call');

new_command.addEventListener('click', function (event) {
  const spawn = require('child_process').spawn;
  const scriptExecution = spawn("python3", ["help.py"]);
  scriptExecution.stdout.on('data', (data) => {
    console.log('success');
  });

  const BrowserWindow = require('electron').remote.BrowserWindow;
  const path = require('path');
  const modalPath = path.join('file://', __dirname, 'message_sent.html')
  let win = new BrowserWindow({ width: 400, height: 320 })
  win.on('close', function () { win = null })
  win.loadURL(modalPath)
  win.show()
})