const { app, BrowserWindow, nativeTheme, ipcMain, dialog } = require('electron')

let win = null

function createWindow () {
  win = new BrowserWindow({
    width: 770,
    height: 650,
    show: false,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation:false
      // enableRemoteModule: true
    }
  })
  nativeTheme.themeSource = 'light'
  win.loadFile('views/html/home.html')
  win.on('ready-to-show', () => {
    win.show()
  })
  const fs = require('fs')
  const path = require('path')
  const dir = path.join(app.getPath('userData'), 'data')

  if  (!fs.existsSync(dir)){
    fs.mkdir(dir, (err) => {
      if (err) {
        alert(err)
      }
      var analysiData = {
        analysiType: null,
        materialType: null,
        materialProps: null,
        geometryType: null,
        geometryProps: null,
        meshType: null,
        meshProps: null,
        boundaryConditionsType: null,
        boundaryConditionsProps: null,
        loadType: null,
        loadProps: null
      }
      fs.writeFileSync(path.join(dir, 'analysiData.json'), JSON.stringify(analysiData))
    })
  }
}

app.whenReady().then(createWindow)

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow()
  }
})

ipcMain.on('create-window', (event, arg) => {
  const newWin = new BrowserWindow({
    width: arg.width,
    height: arg.height,
    parent: win,
    maximizable: false,
    minimizable: false,
    show: false,
    webPreferences: {
      nodeIntegration: true
    }
  })
  newWin.loadFile(arg.path)
  newWin.on('ready-to-show', () => {newWin.show()})
  newWin.setMenu(null)
})

ipcMain.on('delete-current-window', () => {
  BrowserWindow.getFocusedWindow().close()
})

ipcMain.on('get-user-data', (event) => {
  event.returnValue = app.getPath('userData')
})

ipcMain.on('create-dialog', (event, args) => {
  dialog.showErrorBox(args.title, args.description)
})
