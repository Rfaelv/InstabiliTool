const { ipcRenderer } = require('electron')
// const fs = require('fs')
// const path = require('path')
const {writeData, readData} = require('../../modules/writeAndReadData')
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
            ipcRenderer.send('create-dialog', {title: window.i18n.__('Fill in all fields.'), description: ''})
            props[key].focus()
            return

        } else if (key == 'name') {
            const model = readData('model.json')

            for (material of model.materials) {
                if (props.name.value == material.tag) {
                    ipcRenderer.send('create-dialog', {title: window.i18n.__('This name has already been used.'), description: ''})
                    props.name.value = ""
                    props.name.focus()
                    return
                }
            }
        }
    }
    var model = readData('model.json')
    model.materials.push({
        tag: props.name.value,
        materialType: {isotropic: true, orthotropic: false, anisotropic: false},
        materialProperties: {
            E: parseFloat(props.E.value.replace(',', '.')),
            v: parseFloat(props.v.value.replace(',', '.')),
            dens: parseFloat(props.dens.value.replace(',', '.'))
        }
    })

    writeData(model, 'model.json')
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
            ipcRenderer.send('create-dialog', {title: window.i18n.__('Fill in all fields.'), description: ''})
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
    var model = readData('model.json')
    for (let i in model.materials) {
        if (currentTag == model.materials[i].tag) {
            model.materials.splice(i, 1, material)
        }
    }

    writeData(model, 'model.json')
    ipcRenderer.send('delete-current-window')
}

function cancel() {
    ipcRenderer.send('delete-current-window')
}

function fillFields() {
    const currentTag = localStorage.getItem('selected-material')
    const model = readData('model.json')
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
