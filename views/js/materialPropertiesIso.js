const { ipcRenderer, dialog } = require('electron')
const fs = require('fs')
const path = require('path')


const applybutton = document.getElementById('apply')
applybutton.addEventListener('click', setMaterialProperties)

const cancelbutton = document.getElementById('cancel')
cancelbutton.addEventListener('click', cancel)

document.getElementById('elasticModule').focus()

function setMaterialProperties() {
    var props = []
    props.push(document.getElementById('elasticModule'))
    props.push(document.getElementById('poisson'))
    props.push(document.getElementById('density'))

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
    analysiData.materialProps = {
        E: parseFloat(props[0].value.replace(',', '.')),
        v: parseFloat(props[1].value.replace(',', '.')),
        dens: parseFloat(props[2].value.replace(',', '.'))
    }
    analysiData.materialType = 'iso'
    fs.writeFileSync(path.join(userDataPath, 'data/analysiData.json'), JSON.stringify(analysiData))
    ipcRenderer.send('delete-current-window')
}


function cancel() {
    ipcRenderer.send('delete-current-window')
}