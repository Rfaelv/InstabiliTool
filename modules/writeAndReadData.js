const electron = require('electron')
const app = electron.app ? electron.app : electron.remote.app
const dialog = electron.dialog? electron.dialog: electron.remote.dialog
const fs = require('fs')
const path = require('path')
var i18n = new(require('../translations/i18n'))

function writeData(data, name) {
    const userDataPath = app.getPath('userData')
    try {
        fs.writeFileSync(path.join(userDataPath, 'data/', name), JSON.stringify(data))
    } catch (err) {
        dialog.showErrorBox(i18n.__('Error'), err.message)
    }
}

function readData(name) {
    const userDataPath = app.getPath('userData')
    try {
        const jsonData = fs.readFileSync(path.join(userDataPath, 'data/', name), 'utf8')
        var data = JSON.parse(jsonData)
        return data
    } catch (err) {
        dialog.showErrorBox(i18n.__('Error'), err.message)
    }
}

module.exports = {writeData, readData}