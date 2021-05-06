const { ipcRenderer } = require('electron')
const fs = require('fs')
const path = require('path')
var currentTag = null


const applybutton = document.getElementById('apply')
if (localStorage.getItem('selected-material') && localStorage.getItem('selected-material') != '') {
    fillFields()
    applybutton.addEventListener('click', replaceMaterialProperties)
    currentTag = localStorage.getItem('selected-material')
    localStorage.setItem('selected-material', '')
} else {
    applybutton.addEventListener('click', setMaterialProperties)
}

const cancelbutton = document.getElementById('cancel')
cancelbutton.addEventListener('click', cancel)

document.getElementById('name').focus()

function setMaterialProperties() {
    const props = document.getElementsByName('matrix')
    const density = document.getElementById('density')
    const name = document.getElementById('name')

    for (let i = 0; i < props.length; i++) {
        if (props[i].value == '' || density.value == '') {
            ipcRenderer.send('create-dialog', {title: 'Erro', description: 'Preencha todos os campos.'})
            props[i].focus()
            return
        }
    }
    if (name.value == '') {
        ipcRenderer.send('create-dialog', {title: 'Erro', description: 'Preencha todos os campos.'})
            name.focus()
            return
    } else {
        const model = readModel()

        for (material of model.materials) {
            if (name.value == material.tag) {
                ipcRenderer.send('create-dialog', {title: 'Erro', description: 'Esse nome já está sendo usado.'})
                name.value = ""
                name.focus()
                return
            }
        }
    }

    var model = readModel()
    var matrix = []
   
    for (let i = 0 ; i < props.length; i++) {
        matrix.push(parseFloat(props[i].value.replace(',', '.')))
    }
    model.materials.push({
        tag: name.value,
        materialType: {isotropic: false, orthotropic: false, anisotropic: true},
        materialProperties: {stiffnessMatrix: matrix, dens: density.value }
    })

    writeModel(model)
    ipcRenderer.send('delete-current-window')
}

function replaceMaterialProperties() {
    const props = document.getElementsByName('matrix')
    const density = document.getElementById('density')
    const name = document.getElementById('name')

    for (let i = 0; i < props.length; i++) {
        if (props[i].value == '' || density.value == '') {
            ipcRenderer.send('create-dialog', {title: 'Erro', description: 'Preencha todos os campos.'})
            props[i].focus()
            return
        }
    }
    var matrix = []
    for (let i = 0 ; i < props.length; i++) {
        matrix.push(parseFloat(props[i].value.replace(',', '.')))
    }
    const material = {
        tag: name.value,
        materialType: {isotropic: false, orthotropic: false, anisotropic: true},
        materialProperties: {stiffnessMatrix: matrix, dens: density.value }
    }
    var model = readModel()
    for (let i in model.materials) {
        if (currentTag == model.materials[i].tag) {
            model.materials.splice(i, 1, material)
        }
    }

    writeModel(model)
    ipcRenderer.send('delete-current-window')
}

function cancel() {
    ipcRenderer.send('delete-current-window')
}

function fillFields() {
    const currentTag = localStorage.getItem('selected-material')
    var props = document.getElementsByName('matrix')
    const model = readModel()

    for (material of model.materials) {
        if (material.tag == currentTag) {
            for (let i = 0 ; i < props.length; i++) {
                props[i].value = material.materialProperties.stiffnessMatrix[i]
            }
            document.getElementById('name').value = material.tag
            document.getElementById('density').value = material.materialProperties.dens

            return
        }
    }
}

function writeModel(model) {
    const userDataPath = ipcRenderer.sendSync('get-user-data')
    fs.writeFileSync(path.join(userDataPath, 'data/model.json'), JSON.stringify(model), function(err) {
        ipcRenderer.send('create-dialog', {title: 'Erro', description: err})
    })
}

function readModel() {
    const userDataPath = ipcRenderer.sendSync('get-user-data')
    const jsonData = fs.readFileSync(path.join(userDataPath, 'data/model.json'), 'utf8', function(err) {
        ipcRenderer.send('create-dialog', {title: 'Erro', description: err})
    })
    var model = JSON.parse(jsonData)
    return model
}