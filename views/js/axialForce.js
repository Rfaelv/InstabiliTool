const { ipcRenderer } = require('electron')
const {writeData, readData} = require('../../modules/writeAndReadData')

document.querySelector('#x').focus()

const applybutton = document.getElementById('apply')
applybutton.addEventListener('click', setLoadCondition)

const cancelbutton = document.getElementById('cancel')
cancelbutton.addEventListener('click', cancel)

function setLoadCondition() {
    const x = document.getElementById('x')
    const y = document.getElementById('y')
    if (x.value == '' || y.value == '') {
        ipcRenderer.send('create-dialog', {title: window.i18n.__('Fill in all fields.'), description: ''})
        if (x.value == '') {x.focus()} else {y.focus()}
        return
    }
    var model = readData('model.json')
    model.loadType.normal = true
    model.loadType.bending = false

    model.loadProperties = {
        x: parseFloat(x.value.replace(',', '.')),
        y: parseFloat(y.value.replace(',', '.'))
    }

    writeData(model, 'model.json')
    ipcRenderer.send('delete-current-window')
}

function cancel() {
    ipcRenderer.send('delete-current-window')
}