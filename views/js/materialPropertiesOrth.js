const { ipcRenderer } = require('electron')
const fs = require('fs')
const path = require('path')


const applybutton = document.getElementById('apply')
applybutton.addEventListener('click', setMaterialProperties)

const cancelbutton = document.getElementById('cancel')
cancelbutton.addEventListener('click', cancel)

document.getElementById('elasticModulex').focus()

function setMaterialProperties() {
    var props = []
    props.push(document.getElementById('elasticModulex'))
    props.push(document.getElementById('elasticModuley'))
    props.push(document.getElementById('elasticModulez'))
    props.push(document.getElementById('poissonxy'))
    props.push(document.getElementById('poissonyz'))
    props.push(document.getElementById('poissonzx'))
    props.push(document.getElementById('Gxy'))
    props.push(document.getElementById('Gyz'))
    props.push(document.getElementById('Gzx'))
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
        Ex: parseFloat(props[0].value.replace(',', '.')),
        Ey: parseFloat(props[1].value.replace(',', '.')),
        Ez: parseFloat(props[2].value.replace(',', '.')),
        vxy: parseFloat(props[3].value.replace(',', '.')),
        vyz: parseFloat(props[4].value.replace(',', '.')),
        vzx: parseFloat(props[5].value.replace(',', '.')),
        Gxy: parseFloat(props[6].value.replace(',', '.')),
        Gyz: parseFloat(props[7].value.replace(',', '.')),
        Gzx: parseFloat(props[8].value.replace(',', '.')),
        dens: parseFloat(props[9].value.replace(',', '.'))
    }
    analysiData.materialType = 'orth'
    fs.writeFileSync(path.join(userDataPath, 'data/analysiData.json'), JSON.stringify(analysiData))
    ipcRenderer.send('delete-current-window')
}


function cancel() {
    ipcRenderer.send('delete-current-window')
}