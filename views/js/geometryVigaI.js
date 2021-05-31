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
            ipcRenderer.send('create-dialog', {title: window.i18n.__('Fill in all fields.'), description: ''})
            label.focus()
            return
        }
    }
    
    var model = readData('model.json')
    for (key in model.sectionType) {
        if (key == 'I') {
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
    var inputStatus = JSON.parse(localStorage.getItem('input-status'))
    inputStatus.section = true
    inputStatus.matAssign = false
    localStorage.setItem('input-status', JSON.stringify(inputStatus))
    ipcRenderer.send('delete-current-window')
}

function cancel() {
    ipcRenderer.send('delete-current-window')
}