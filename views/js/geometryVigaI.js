const { ipcRenderer, dialog } = require('electron')
const fs = require('fs')
const path = require('path')


const applybutton = document.getElementById('apply')
applybutton.addEventListener('click', setGeometry)

const cancelbutton = document.getElementById('cancel')
cancelbutton.addEventListener('click', cancel)

document.getElementById('d').focus()


function setGeometry() {
    const input = document.getElementsByName('input')

    for (let i = 0; i < input.length; i++) {
        if (input[i].value == '') {
            ipcRenderer.send('create-dialog', {title: 'Erro', description: 'Preencha todos os campos.'})
            input[i].focus()
            return
        }
    }

    const userDataPath = ipcRenderer.sendSync('get-user-data')
    const jsonData = fs.readFileSync(path.join(userDataPath, 'data/analysiData.json'), 'utf8')
    var analysiData = JSON.parse(jsonData)
    analysiData.geometryProps = {
        d: parseFloat(input[0].value.replace(',', '.')),
        bfs: parseFloat(input[1].value.replace(',', '.')),
        bfi: parseFloat(input[2].value.replace(',', '.')),
        tw: parseFloat(input[3].value.replace(',', '.')),
        tfs: parseFloat(input[4].value.replace(',', '.')),
        tfi: parseFloat(input[5].value.replace(',', '.')),
        L: parseFloat(input[6].value.replace(',', '.'))
    }
    analysiData.geometryType = 'i'
    fs.writeFileSync(path.join(userDataPath, 'data/analysiData.json'), JSON.stringify(analysiData))
    ipcRenderer.send('delete-current-window')
}

function cancel() {
    ipcRenderer.send('delete-current-window')
}