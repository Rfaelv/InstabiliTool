const { ipcRenderer, dialog } = require('electron')
const fs = require('fs')
const path = require('path')
const {writeData, readData} = require('../../modules/writeAndReadData')

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
    var inputStatus = JSON.parse(localStorage.getItem('input-status'))

    for (key in model.sectionType) {
        if (key == 'I') {
            if (!model.sectionType[key]) {
                model.boundaryConditions = {}
                inputStatus.bd = false
            }
            model.sectionType[key] = true
        } else {
            model.sectionType[key] = false
        }
    }
    model.sectionProperties = {
        d: parseFloat(input[0].value.replace(',', '.')),
        bfs: parseFloat(input[1].value.replace(',', '.')),
        bfi: parseFloat(input[2].value.replace(',', '.')),
        tw: parseFloat(input[3].value.replace(',', '.')),
        tfs: parseFloat(input[4].value.replace(',', '.')),
        tfi: parseFloat(input[5].value.replace(',', '.')),
        L: parseFloat(input[6].value.replace(',', '.'))
    }

    writeData(model, 'model.json')
   
    inputStatus.section = true
    inputStatus.matAssign = false
    localStorage.setItem('input-status', JSON.stringify(inputStatus))
    ipcRenderer.send('delete-current-window')
}

function cancel() {
    ipcRenderer.send('delete-current-window')
}

function setModelData() {
    const model = readData('model.json')

    if (model.sectionType.I) {
        for (let key in model.sectionProperties) {
            document.getElementById(key).value = model.sectionProperties[key]
        }
    }
}