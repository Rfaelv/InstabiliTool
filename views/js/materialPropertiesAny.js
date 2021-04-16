const { ipcRenderer } = require('electron')
const fs = require('fs')
const path = require('path')


const applybutton = document.getElementById('apply')
applybutton.addEventListener('click', setMaterialProperties)

const cancelbutton = document.getElementById('cancel')
cancelbutton.addEventListener('click', cancel)

document.getElementsByName('matrix')[0].focus()

function setMaterialProperties() {
    const props = document.getElementsByName('matrix')

    for (let i = 0; i < props.length; i++) {
        if (props[i].value == '') {
            ipcRenderer.send('create-dialog', {title: 'Erro', description: 'Preencha todos os campos.'})
            props[i].focus()
            return
        }
    }

    const userDataPath = ipcRenderer.sendSync('get-user-data')
    const jsonData = fs.readFileSync(path.join(userDataPath, 'data/analysiData.json'), 'utf8')
    var analysiData = JSON.parse(jsonData)
    var matrix = []
   
    for (let i = 0 ; i < props.length; i++) {
        matrix.push(parseFloat(props[i].value.replace(',', '.')))
    }

    analysiData.materialProps = matrix
    analysiData.materialType = 'Any'
    fs.writeFileSync(path.join(userDataPath, 'data/analysiData.json'), JSON.stringify(analysiData))
    ipcRenderer.send('delete-current-window')
}


function cancel() {
    ipcRenderer.send('delete-current-window')
}