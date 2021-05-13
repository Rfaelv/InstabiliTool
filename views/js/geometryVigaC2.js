const { ipcRenderer, dialog } = require('electron')
const fs = require('fs')
const path = require('path')
const {writeData, readData} = require('../../modules/writeAndReadData')

const applybutton = document.getElementById('apply')
applybutton.addEventListener('click', setGeometry)

const cancelbutton = document.getElementById('cancel')
cancelbutton.addEventListener('click', cancel)

document.getElementById('d').focus()


function setGeometry() {
    const input = document.getElementsByName('input')

    for (label of input) {
        if (label.value == '') {
            ipcRenderer.send('create-dialog', {title: 'Erro', description: 'Preencha todos os campos.'})
            label.focus()
            return
        }
    }

    var model = readData('model.json')
    for (key in model.sectionType) {
        if (key == 'C2') {
            model.sectionType[key] = true
        } else {
            model.sectionType[key] = false
        }
    }
    model.sectionProperties = {
        d: parseFloat(input[0].value.replace(',', '.')),
        b: parseFloat(input[1].value.replace(',', '.')),
        t: parseFloat(input[2].value.replace(',', '.')),
        z: parseFloat(input[3].value.replace(',', '.')),
        L: parseFloat(input[4].value.replace(',', '.'))
    }
    writeData(model, 'model.json')
    ipcRenderer.send('delete-current-window')
}

function cancel() {
    ipcRenderer.send('delete-current-window')
}