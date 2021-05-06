const { ipcRenderer, dialog } = require('electron')
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
    var props = {}
    props.E = document.getElementById('elasticModule')
    props.v = document.getElementById('poisson')
    props.dens = document.getElementById('density')
    props.name = document.getElementById('name')

    for (let key in props) {
        if (props[key].value == '') {
            ipcRenderer.send('create-dialog', {title: 'Erro', description: 'Preencha todos os campos.'})
            props[key].focus()
            return

        } else if (key == 'name') {
            const model = readModel()

            for (material of model.materials) {
                if (props.name.value == material.tag) {
                    ipcRenderer.send('create-dialog', {title: 'Erro', description: 'Esse nome já está sendo usado.'})
                    props.name.value = ""
                    props.name.focus()
                    return
                }
            }
        }
    }
    var model = readModel()
    model.materials.push({
        tag: props.name.value,
        materialType: {isotropic: true, orthotropic: false, anisotropic: false},
        materialProperties: {
            E: parseFloat(props.E.value.replace(',', '.')),
            v: parseFloat(props.v.value.replace(',', '.')),
            dens: parseFloat(props.dens.value.replace(',', '.'))
        }
    })

    writeModel(model)
    ipcRenderer.send('delete-current-window')
}

function replaceMaterialProperties() {
    var props = {}
    props.E = document.getElementById('elasticModule')
    props.v = document.getElementById('poisson')
    props.dens = document.getElementById('density')
    props.name = document.getElementById('name')

    for (let key in props) {
        if (props[key].value == '') {
            ipcRenderer.send('create-dialog', {title: 'Erro', description: 'Preencha todos os campos.'})
            props[key].focus()
            return

        }
    }
    const material = {
        tag: props.name.value,
        materialType: {isotropic: true, orthotropic: false, anisotropic: false},
        materialProperties: {
            E: parseFloat(props.E.value.replace(',', '.')),
            v: parseFloat(props.v.value.replace(',', '.')),
            dens: parseFloat(props.dens.value.replace(',', '.'))
        }
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
    const model = readModel()
    for (material of model.materials) {
        if (material.tag == currentTag) {
            document.getElementById('elasticModule').value = material.materialProperties.E
            document.getElementById('poisson').value = material.materialProperties.v
            document.getElementById('density').value = material.materialProperties.dens
            document.getElementById('name').value = material.tag

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