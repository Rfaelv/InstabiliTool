const { app, electron, Menu, dialog, BrowserWindow, ipcRenderer } = require('electron')
const shell = require('electron').shell
const fs = require('fs')
const path = require('path')
var i18n = new(require('../translations/i18n'))
const localState  = new(require('../modules/localState'))
const { readData, writeData } = require('../modules/writeAndReadData')
const { clearModel } = require('../modules/clearModel')

localState.createIfNotExist()
localState.clear()
localState.set('model', JSON.stringify(readData('model.json')))

const template = [
    {
      label: i18n.__('File'),
      submenu: [
        {
          label: i18n.__('About'),
          click() {
            shell.openExternal("https://rfaelv.github.io/InstabiliTool/about")
          },
        },
        {type: 'separator'},
        {
          label: i18n.__('New'),
          click() {
            newFile()
          },
          accelerator: 'Ctrl+N'
        },
        {
          label: i18n.__('Open'),
          click() {
            openFile()
          },
          accelerator: 'Ctrl+O'
        },
        {
          label: i18n.__('Save'),
          click() {
            saveFile()
          },
          accelerator: 'Ctrl+S'
        },
        {
          label: i18n.__('Save as...'),
          click() {
            saveFileAs()
          },
        },
        {type: 'separator'},
        {
            label: i18n.__('Quit'),
            click() {
              app.quit()
            },
          }
      ]
    },
    {
        label: i18n.__('Options'),
        submenu: [
            {
              label: i18n.__('Linear analysis'),
              click() {
                createWindow(260, 180, './views/html/linearAnalysisOptions.html')
              }
            },
            {
              label: i18n.__('Nonlinear analysis'),
              click() {
                createWindow(300, 220, './views/html/nonlinearAnalysisOptions.html')
              }
            },
            {type: 'separator'},
            {
              label: i18n.__('General'),
              click() {
                createWindow(510, 300, './views/html/generalAnalysisOptions.html')
              }
            }
        ]
    },
    {
        label: i18n.__('Definitions'),
        submenu: [
            {
                label: i18n.__('Units'),
                click() {
                  createWindow(250, 180, './views/html/units.html')
                }
            },
            {
                label: i18n.__('Material axes'),
                click() {
                  createWindow(320, 320, './views/html/materialAxes.html')
                }
            }
        ]
    },
    {
      label: i18n.__('Help'),
      submenu: [
        {
          label: i18n.__('Documentation'),
          click() {
            shell.openExternal('https://rfaelv.github.io/InstabiliTool/documentation')
          }
        },
        {
          label: i18n.__('Contact us'),
          click() {
            shell.openExternal("mailto:rafa10031999@gmail.com?subject=&body=");
          }
        }
      ]
    }
]

const menu = Menu.buildFromTemplate(template)
Menu.setApplicationMenu(menu)

function newFile() {
  const mainWin = BrowserWindow.getFocusedWindow()
  const model = JSON.stringify(readData('model.json'))
  const modelState = localState.get('model') 

  if ( model != modelState) {
    dialog.showMessageBox(mainWin, {
      message: i18n.__('The current file has changed. Save changes?'),
      type: 'question',
      buttons: [i18n.__('Save'), i18n.__('Discard'), i18n.__('Cancel')],
      defaultId: 0,
      title: 'InstabiliTool'
    }).then((index) => {
      if (index.response == 0) {
        saveFile()

      } else if (index.response == 2) {
        return

      }
      localState.clear()
      clearModel()
      localState.set('model', JSON.stringify(readData('model.json')))
      mainWin.title = 'InstabiliTool'
      mainWin.reload()

    })
  } else {
    localState.clear()
    clearModel()
    localState.set('model', JSON.stringify(readData('model.json')))
    mainWin.title = 'InstabiliTool'
    mainWin.reload()

  }
}

function openFile() {
  const mainWin = BrowserWindow.getFocusedWindow()
  dialog.showOpenDialog(mainWin, {
    title: i18n.__('Open File'),
    properties: ['openFile'],
    filters: [
        { name: i18n.__('InstabiliTool file'), extensions: ['instt'] },
      ]
  }).then(result => {
    if (result.canceled) {return}

    const filePath = localState.get('file-path')
    
    if (filePath == result.filePaths[0] && result.filePaths[0]) {
      dialog.showMessageBox(mainWin, {
        message: i18n.__('The selected file is already open.'),
        type: 'info',
        buttons: [],
        defaultId: 0,
        title: 'InstabiliTool'
      })
      return
    }
    const model = JSON.stringify(readData('model.json'))
    const modelState = localState.get('model') 

    if ( model != modelState) {
      dialog.showMessageBox(mainWin, {
        message: i18n.__('The current file has changed. Save changes?'),
        type: 'question',
        buttons: [i18n.__('Save'), i18n.__('Discard'), i18n.__('Cancel')],
        defaultId: 0,
        title: 'InstabiliTool'
      }).then((index) => {
        var response
        if (index.response == 0) {
          response = saveFile()

        } else if (index.response == 2) {
          return 

        }
        if (response.canceled) {return}

        localState.set('file-path', result.filePaths[0])
        const newmodelState = JSON.parse(fs.readFileSync(result.filePaths[0], 'utf8'))
        writeData(newmodelState, 'model.json')
        localState.set('model', JSON.stringify(newmodelState))
        mainWin.title = `InstabiliTool - ${result.filePaths[0].split('\\').pop().split('.')[0]}`
        mainWin.reload()

      })
    } else {
      localState.set('file-path', result.filePaths[0])
      const newmodelState = JSON.parse(fs.readFileSync(result.filePaths[0], 'utf8'))
      writeData(newmodelState, 'model.json')
      localState.set('model', JSON.stringify(newmodelState))
      mainWin.title = `InstabiliTool - ${result.filePaths[0].split('\\').pop().split('.')[0]}`
      mainWin.reload()

    }
  })
}

function saveFile() {
  const filePath = localState.get('file-path')
  const mainWin = BrowserWindow.getFocusedWindow()
  
  if (filePath && fs.existsSync(filePath)) {
    try {
      var model = readData('model.json')
      fs.writeFileSync(filePath, JSON.stringify(model))
      mainWin.title = `InstabiliTool - ${filePath.split('\\').pop().split('.')[0]}`
      localState.set('model', JSON.stringify(model))

    } catch (err) {
      dialog.showErrorBox(i18n.__('Error'), err.message)

    }
  
  } else {
    return saveFileAs()

  }
}

function saveFileAs() {
  const mainWin = BrowserWindow.getFocusedWindow()
  const result = dialog.showSaveDialogSync(mainWin, {
    title: i18n.__('Save File'),
    properties: ['openDirectory'],
    defaultPath: i18n.__('instability-analysi'),
    filters: [
        { name: i18n.__('InstabiliTool file'), extensions: ['instt'] },
    ]
  })
  response = {}
  response.canceled = true

  if (result == undefined) {return response}

  try {
    var model = readData('model.json')
  } catch (err) {
    dialog.showErrorBox(i18n.__('Error'), err.message)
    return
  }

  try {
    fs.writeFileSync(result, JSON.stringify(model))
    mainWin.title = `InstabiliTool - ${result.split('\\').pop().split('.')[0]}`
    localState.set('file-path', result)
    localState.set('model', JSON.stringify(model))
    
  } catch (err) {
    if (err.message != 'ENOENT: no such file or directory, open') {
      dialog.showErrorBox(i18n.__('Error'), err.message)
    }
  }
  // })
}

function createWindow(width, height, filePath) {
  const newWin = new BrowserWindow({
    width: width,
    height: height,
    parent: BrowserWindow.getFocusedWindow(),
    maximizable: false,
    minimizable: false,
    show: false,
    webPreferences: {
      nodeIntegration: true,
      enableRemoteModule: true
    }
  })
  newWin.loadFile(filePath)
  newWin.on('ready-to-show', () => {newWin.show()})
  newWin.setMenu(null)
  // newWin.webContents.openDevTools()
}
