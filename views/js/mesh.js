const { ipcRenderer, dialog } = require('electron')
const fs = require('fs')
const path = require('path')


const applybutton = document.getElementById('apply')
applybutton.addEventListener('click', setMeshProps)

const cancelbutton = document.getElementById('cancel')
cancelbutton.addEventListener('click', cancel)

document.getElementById('elementSize').focus()


function setMeshProps() {
    const elementSize = document.getElementById('elementSize')
    const elementMethod = document.getElementsByName('method')

    if (elementSize.value == '' || (!elementMethod[0].checked && !elementMethod[1].checked)) {
        ipcRenderer.send('create-dialog', {title: 'Erro', description: 'Preencha todos os campos.'})
        if (elementSize.value == '') {
            elementSize.focus()
        }
        return
    }

    const userDataPath = ipcRenderer.sendSync('get-user-data')
    const jsonData = fs.readFileSync(path.join(userDataPath, 'data/analysiData.json'), 'utf8')
    var analysiData = JSON.parse(jsonData)
    analysiData.meshProps = {
        elementSize: parseFloat(elementSize.value.replace(',', '.')),
        method: parseFloat((elementMethod[0].checked? 0 : 1)),
    }
    fs.writeFileSync(path.join(userDataPath, 'data/analysiData.json'), JSON.stringify(analysiData))
    ipcRenderer.send('delete-current-window')
}


function cancel() {
    ipcRenderer.send('delete-current-window')
}