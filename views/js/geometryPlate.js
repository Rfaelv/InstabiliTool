const { ipcRenderer, dialog } = require('electron')
// const fs = require('fs')
// const path = require('path')
const { writeData, readData } = require('../../modules/writeAndReadData')


const applybutton = document.getElementById('apply')
applybutton.addEventListener('click', setGeometry)

const cancelbutton = document.getElementById('cancel')
cancelbutton.addEventListener('click', cancel)

document.getElementById('d').focus()

window.addEventListener('load', () => {
    setModelData()
})

function setGeometry() {
    const input = document.getElementsByName('input')

    for (label of input) {
        if (label.value == '') {
            ipcRenderer.send('create-dialog', {title: window.i18n.__('Fill in all fields.'), description: ''})
            label.focus()
            return
        }
    }

    var model = readData('model.json')

    for (key in model.sectionType) {
        if (key == 'plate') {
            if (!model.sectionType[key]) {
                if (model.boundaryConditions.personalized) {
                    model.boundaryConditions = {}
                }
            }
            model.sectionType[key] = true
        } else {
            model.sectionType[key] = false
        }
    }
    model.sectionProperties = {
        d: parseFloat(input[0].value.replace(',', '.')),
        t: parseFloat(input[1].value.replace(',', '.')),
        L: parseFloat(input[2].value.replace(',', '.'))
    }
    writeData(model, 'model.json')
    
    ipcRenderer.send('delete-current-window')
}

function cancel() {
    ipcRenderer.send('delete-current-window')
}

function setModelData() {
    const model = readData('model.json')

    if (model.sectionType.plate) {
        for (let key in model.sectionProperties) {
            document.getElementById(key).value = model.sectionProperties[key]
        }
    }
}