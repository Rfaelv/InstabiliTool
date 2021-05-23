const { ipcRenderer } = require('electron')
const fs = require('fs')
const path = require('path')
const {writeData, readData} = require('../../modules/writeAndReadData')
const i18n = require('../../translations/i18n')

setTitle()

document.getElementById('add')
    .addEventListener('click', add)
document.getElementById('edit')
    .addEventListener('click', edit)
document.getElementById('delete')
    .addEventListener('click', del)
document.getElementById('ok')
    .addEventListener('click', finalize)

window.addEventListener('load', refreshData)
window.addEventListener('focus', refreshData)

function add() {
    openInputPropertieWindow()
}

function edit() {
    if (document.querySelector('input[name="materialList"]:checked')) {
        localStorage.setItem('selected-material', document.querySelector('input[name="materialList"]:checked').value)
        openInputPropertieWindow()
    }       
}

function del() {
    if (document.querySelector('input[name="materialList"]:checked')) {
        removeMaterial(document.getElementsByName('selected')[0].textContent)
        const list = document.getElementById('list')
        list.removeChild(document.querySelector('input[name="materialList"]:checked'))
        list.removeChild(document.getElementsByName('selected')[0])
    }     
}

function finalize() {
    ipcRenderer.send('delete-current-window')
}
function refreshData() {
    generateList()
}

function generateList() {
    var tagList = []

    const model = readData('model.json')
    const materialData = model.materials

    document.getElementById('list').innerHTML = ''

    for (var i in materialData) {
        if (materialData[i].materialType[localStorage.getItem('current-material-type')]) {
            const tag = materialData[i].tag
            var radio = document.createElement('input')
            radio.setAttribute('type', "radio")
            radio.setAttribute('class', "form-check-input")
            radio.setAttribute('id', tag)
            radio.setAttribute('name', 'materialList')
            radio.setAttribute('value', tag)
            radio.onchange = select

            var label = document.createElement('label')
            label.setAttribute('class', 'materialTag')
            label.setAttribute('for', tag)
            label.setAttribute('name', 'non-selected')

            var materialTag = document.createTextNode(tag)

            label.appendChild(materialTag)

            document.getElementById('list').appendChild(radio)
            document.getElementById('list').appendChild(label)

            tagList.push([radio, label])
        }
        function select() {
            for (let i in tagList) {
                if (tagList[i][0].checked) {
                    tagList[i][1].setAttribute('name', 'selected')

                } else {
                    tagList[i][1].setAttribute('name', 'non-selected')

                }
            }
        }
    }
}

function setTitle() {
    const title = document.getElementsByTagName('title')
    var text = null
    if (localStorage.getItem('current-material-type') == 'isotropic') {
        text = document.createTextNode(window.i18n.__('Isotropic material'))

    } else if (localStorage.getItem('current-material-type') == 'orthotropic') {
        text = document.createTextNode(window.i18n.__('Orthotropic material'))

    } else if (localStorage.getItem('current-material-type') == 'anisotropic') {
        text = document.createTextNode(window.i18n.__('Anisotropic material'))
        
    }
    title[0].appendChild(text)
}

function openInputPropertieWindow() {
    if (localStorage.getItem('current-material-type') == 'isotropic') {
        ipcRenderer.send('create-window', {
            width:200,
            height:250,
            path:'views/html/materialPropertiesIso.html'
        })

    } else if (localStorage.getItem('current-material-type') == 'orthotropic') {
        ipcRenderer.send('create-window', {
            width:210,
            height:420,
            path:'views/html/materialPropertiesOrth.html'
        })

    } else if (localStorage.getItem('current-material-type') == 'anisotropic') {
        ipcRenderer.send('create-window', {
            width:820,
            height:350,
            path:'views/html/materialPropertiesAny.html'
        })
    }
}

function removeMaterial(materialTag) {
    var model = readData('model.json')
    for (let i in model.materials) {
        if (model.materials[i].tag == materialTag) {
            model.materials.splice(i, 1)
            writeData(model, 'model.json')
            return
        }
    }
}
