const electron = require('electron')
const app = electron.app ? electron.app : electron.remote.app
const dialog = electron.dialog? electron.dialog : electron.remote.dialog
const fs = require('fs')
const path = require('path')
var i18n = new(require('../translations/i18n'))

module.exports = class LocalState {
  set(key, value) {
    const userDataPath = app.getPath('userData')
    if  (!fs.existsSync(path.join(userDataPath, 'data/localstatedata.json'))) {
      var saveData = {}
      saveData[key] = value
  
      try {
        fs.writeFileSync(path.join(userDataPath, 'data/localstatedata.json'), JSON.stringify(saveData))
  
      } catch (err) {
        dialog.showErrorBox(i18n.__('Error'), err.message)
  
      }
  
    } else {
      try {
        var saveData = JSON.parse(fs.readFileSync(path.join(userDataPath, 'data/localstatedata.json'), 'utf8'))
        saveData[key] = value
        fs.writeFileSync(path.join(userDataPath, 'data/localstatedata.json'), JSON.stringify(saveData))
  
      } catch (err) {
        dialog.showErrorBox(i18n.__('Error'), err.message)
  
      }
    }
  }
  
  get(key) {
    const userDataPath = app.getPath('userData')
    try {
      var saveData = JSON.parse(fs.readFileSync(path.join(userDataPath, 'data/localstatedata.json'), 'utf8'))
      return saveData[key]
  
    } catch (err) {
      dialog.showErrorBox(i18n.__('Error'), err.message)
  
    }
  }
  
  clear() {
    const userDataPath = app.getPath('userData')
    try {
      var saveData = JSON.parse(fs.readFileSync(path.join(userDataPath, 'data/localstatedata.json'), 'utf8'))
      saveData = {}
      fs.writeFileSync(path.join(userDataPath, 'data/localstatedata.json'), JSON.stringify(saveData))

    } catch (err) {
      dialog.showErrorBox(i18n.__('Error'), err.message)

    }
  }
}