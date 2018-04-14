const glob = require('glob')
const electron = require('electron')
const app = electron.app
const BrowserWindow = electron.BrowserWindow

const path = require('path')
const url = require('url')

let mainWindow

function createWindow () {
  mainWindow = new BrowserWindow({width: 1080, height:724});

  mainWindow.loadURL(url.format({
    pathname: path.join(__dirname, 'index.html'),
    protocol: 'file:',
    slashes: true
  }))

  mainWindow.on('closed', function () {
    mainWindow = null
  })

  const spawn = require('child_process').spawn;
  const scriptExecution = spawn("python", ["setToken.py"]);
          // Handle normal output
          scriptExecution.stdout.on('data', (data) => {
            console.log(String.fromCharCode.apply(null, data));
          });

  //mainWindow.openDevTools();
}

app.on('ready', createWindow);
app.on('window-all-closed', () => {
    app.quit();
});

app.disableHardwareAcceleration();

app.on('activate', function () {
  if (mainWindow === null) {
    createWindow()
  }
})
