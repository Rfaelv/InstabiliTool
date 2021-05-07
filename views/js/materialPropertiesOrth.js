const { ipcRenderer } = require('electron')
const fs = require('fs')
const path = require('path')
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
    var props = getInput()

    for (let key in props) {
        if (props[key].value == '') {
            ipcRenderer.send('create-dialog', {title: 'Erro', description: 'Preencha todos os campos.'})
            props[key].focus()
            return

        } else if (key == 'name') {
            const model = readData('model.json')

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

    var model = readData('model.json')
    model.materials.push({
        tag: props.name.value,
        materialType: {isotropic: false, orthotropic: true, anisotropic: false},
        materialProperties: {
            Ex: parseFloat(props.Ex.value.replace(',', '.')),
            Ey: parseFloat(props.Ey.value.replace(',', '.')),
            Ez: parseFloat(props.Ez.value.replace(',', '.')),
            vxy: parseFloat(props.vxy.value.replace(',', '.')),
            vyz: parseFloat(props.vyz.value.replace(',', '.')),
            vxz: parseFloat(props.vxz.value.replace(',', '.')),
            Gxy: parseFloat(props.Gxy.value.replace(',', '.')),
            Gyz: parseFloat(props.Gyz.value.replace(',', '.')),
            Gxz: parseFloat(props.Gxz.value.replace(',', '.')),
            dens: parseFloat(props.dens.value.replace(',', '.'))
        }
    })

    writeData(model, 'model.json')
    ipcRenderer.send('delete-current-window')
}

function replaceMaterialProperties() {
    var props = getInput()

    for (let key in props) {
        if (props[key].value == '') {
            ipcRenderer.send('create-dialog', {title: 'Erro', description: 'Preencha todos os campos.'})
            props[key].focus()
            return

        }
    }
    const material = {
        tag: props.name.value,
        materialType: {isotropic: false, orthotropic: true, anisotropic: false},
        materialProperties: {
            Ex: parseFloat(props.Ex.value.replace(',', '.')),
            Ey: parseFloat(props.Ey.value.replace(',', '.')),
            Ez: parseFloat(props.Ez.value.replace(',', '.')),
            vxy: parseFloat(props.vxy.value.replace(',', '.')),
            vyz: parseFloat(props.vyz.value.replace(',', '.')),
            vxz: parseFloat(props.vxz.value.replace(',', '.')),
            Gxy: parseFloat(props.Gxy.value.replace(',', '.')),
            Gyz: parseFloat(props.Gyz.value.replace(',', '.')),
            Gxz: parseFloat(props.Gxz.value.replace(',', '.')),
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
            document.getElementById('elasticModulex').value = material.materialProperties.Ex
            document.getElementById('elasticModuley').value = material.materialProperties.Ey
            document.getElementById('elasticModulez').value = material.materialProperties.Ez
            document.getElementById('poissonxy').value = material.materialProperties.vxy
            document.getElementById('poissonyz').value = material.materialProperties.vyz
            document.getElementById('poissonxz').value = material.materialProperties.vxz
            document.getElementById('Gxy').value = material.materialProperties.Gxy
            document.getElementById('Gyz').value = material.materialProperties.Gyz
            document.getElementById('Gxz').value = material.materialProperties.Gxz
            document.getElementById('density').value = material.materialProperties.dens
            document.getElementById('name').value = material.tag

            return
        }
    }
}

function getInput() {
    var props = {}
    props.Ex = document.getElementById('elasticModulex')
    props.Ey = document.getElementById('elasticModuley')
    props.Ez = document.getElementById('elasticModulez')
    props.vxy = document.getElementById('poissonxy')
    props.vyz = document.getElementById('poissonyz')
    props.vxz = document.getElementById('poissonxz')
    props.Gxy = document.getElementById('Gxy')
    props.Gyz = document.getElementById('Gyz')
    props.Gxz = document.getElementById('Gxz')
    props.dens = document.getElementById('density')
    props.name = document.getElementById('name')

    return props
}