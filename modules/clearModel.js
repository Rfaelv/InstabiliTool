const fs = require('fs')
const path = require('path')
const electron = require('electron')
const i18n = require('../translations/i18n')
const app = electron.app ? electron.app : electron.remote.app
const dialog = electron.dialog? electron.dialog : electron.remote.dialog
var i18n = new(require('../translations/i18n'))

module.exports = {clearModel}

function clearModel() {
    var model = {
        analysiType: {linear: true, nonlinear: false},
        materials: [],
        sectionType: {I: false, tubular: false, C: false, C2:false, rack: false, angle: false, plate: false},
        sectionProperties: {},
        meshProperties: {type: 0},
        boundaryConditions: {},
        loadType: {bending: true, normal: false},
        loadProperties: {}
    }
      
    const modelPath = path.join(app.getPath('userData'), 'data/model.json')

    try {
        fs.writeFileSync(modelPath, JSON.stringify(model))
    } catch (err) {
        dialog.showErrorBox(i18n.__('Error'), err.message)
    }
}