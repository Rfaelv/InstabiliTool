const { app, BrowserWindow, nativeTheme, ipcMain, dialog} = require('electron')
const process = require('process')

const inputData = process.argv

let win = null

function createWindow () {
  win = new BrowserWindow({
    width: 770,
    height: 650,
    show: false,
    icon: './assets/icons/icon.ico',
    webPreferences: {
      nodeIntegration: true,
      contextIsolation:false,
      enableRemoteModule: true
    }
  })

  require('./menu/mainmenu')
  createModel()
  createSettings()
  setInputModelIfExist()
  // win.webContents.openDevTools()
  nativeTheme.themeSource = 'light'
  win.loadFile('views/html/home.html')
  win.on('ready-to-show', () => {
    setTimeout(() => {win.show()}, 200) 
  })
  // win.show()
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
      nodeIntegration: true,
      enableRemoteModule: true
    }
  })
  newWin.loadFile(arg.path)
  newWin.on('ready-to-show', () => {setTimeout(() =>{newWin.show()}, 200) })
  newWin.setMenu(null)
  // newWin.webContents.openDevTools()
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


function createModel() {
  var model = {
    analysiType: {linear: true, nonlinear: false},
    materials: [],
    sectionType: {I: false, tubular: false, C: false, C2:false, rack: false, angle: false, plate: false},
    sectionProperties: {},
    meshProperties: {type: 0},
    boundaryConditions: {},
    loadType: {bending: true, normal: false},
    loadProperties: {},
    result: {}
    }
  const fs = require('fs')
  const path = require('path')
  const dir = path.join(app.getPath('userData'), 'data')

  if  (!fs.existsSync(dir)){
    fs.mkdir(dir, (err) => {
      if (err) {
        dialog.showErrorBox('Erro', err)
      }
      fs.writeFileSync(path.join(dir, 'model.json'), JSON.stringify(model))
    })
  } else {
    fs.writeFileSync(path.join(dir, 'model.json'), JSON.stringify(model))
  }
}

function createSettings() {
  const settings = {
    linearAnalysis: {
      nmodes: 10
    },
    nonlinearAnalysis: {
      loadFactor: 1.2,
      initialDeformationFactor: 0.1
    },
    general: {
      elementStiffness: 0,
      integrationOption: 2,
      curvedShellFormulation: 0
    }
  }

  const fs = require('fs')
  const path = require('path')
  const dir = path.join(app.getPath('userData'), 'data/settings.json')
  
  if  (!fs.existsSync(dir)){
    fs.writeFileSync(dir, JSON.stringify(settings))
  }
}

function setInputModelIfExist() {
  if (inputData[1] && inputData[1].split('.')[1] == "instt") {
    const inputModelPath = inputData[1]
    const fs = require('fs')

    try {
      const jsonData = fs.readFileSync(inputModelPath, 'utf8')
      const inputModel = JSON.parse(jsonData)

      const model = {
        analysiType: inputModel.analysiType,
        materials: inputModel.materials,
        sectionType: inputModel.sectionType,
        sectionProperties: inputModel.sectionProperties,
        meshProperties: inputModel.meshProperties,
        boundaryConditions: inputModel.boundaryConditions,
        loadType: inputModel.loadType,
        loadProperties: inputModel.loadProperties,
        result: inputModel.result
      }
      writeData(model, 'model.json')
    } catch (err) {
      dialog.showErrorBox(i18n.__('Error'), err.message)
    }
  }
}