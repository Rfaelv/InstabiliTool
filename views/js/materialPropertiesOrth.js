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
    var props = getInput()

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
        materialType: {isotropic: false, orthotropic: true, anisotropic: false},
        materialProperties: {
            Ex: parseFloat(props.Ex.value.replace(',', '.')),
            Ey: parseFloat(props.Ey.value.replace(',', '.')),
            Ez: parseFloat(props.Ez.value.replace(',', '.')),
            vxy: parseFloat(props.vxy.value.replace(',', '.')),
            vyz: parseFloat(props.vyz.value.replace(',', '.')),
            vzx: parseFloat(props.vzx.value.replace(',', '.')),
            Gxy: parseFloat(props.Gxy.value.replace(',', '.')),
            Gyz: parseFloat(props.Gyz.value.replace(',', '.')),
            Gzx: parseFloat(props.Gzx.value.replace(',', '.')),
            dens: parseFloat(props.dens.value.replace(',', '.'))
        }
    })

    writeModel(model)
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
            vzx: parseFloat(props.vzx.value.replace(',', '.')),
            Gxy: parseFloat(props.Gxy.value.replace(',', '.')),
            Gyz: parseFloat(props.Gyz.value.replace(',', '.')),
            Gzx: parseFloat(props.Gzx.value.replace(',', '.')),
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
            document.getElementById('elasticModulex').value = material.materialProperties.Ex
            document.getElementById('elasticModuley').value = material.materialProperties.Ey
            document.getElementById('elasticModulez').value = material.materialProperties.Ez
            document.getElementById('poissonxy').value = material.materialProperties.vxy
            document.getElementById('poissonyz').value = material.materialProperties.vyz
            document.getElementById('poissonzx').value = material.materialProperties.vzx
            document.getElementById('Gxy').value = material.materialProperties.Gxy
            document.getElementById('Gyz').value = material.materialProperties.Gyz
            document.getElementById('Gzx').value = material.materialProperties.Gzx
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

function getInput() {
    var props = {}
    props.Ex = document.getElementById('elasticModulex')
    props.Ey = document.getElementById('elasticModuley')
    props.Ez = document.getElementById('elasticModulez')
    props.vxy = document.getElementById('poissonxy')
    props.vyz = document.getElementById('poissonyz')
    props.vzx = document.getElementById('poissonzx')
    props.Gxy = document.getElementById('Gxy')
    props.Gyz = document.getElementById('Gyz')
    props.Gzx = document.getElementById('Gzx')
    props.dens = document.getElementById('density')
    props.name = document.getElementById('name')

    return props
}