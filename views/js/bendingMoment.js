const { ipcRenderer } = require('electron')
const {writeData, readData} = require('../../modules/writeAndReadData')

document.querySelector('#Lshear').focus()

const radioButton = document.getElementsByName('flexao')
radioButton[0].addEventListener('change', switchImage)
radioButton[1].addEventListener('change', switchImage)

const applybutton = document.getElementById('apply')
applybutton.addEventListener('click', setLoadCondition)

const cancelbutton = document.getElementById('cancel')
cancelbutton.addEventListener('click', cancel)

function switchImage() {
    var img = document.getElementById('image-flexao')
    var div = document.getElementById('input') 
    if (radioButton[0].checked) {
        img.setAttribute('src', "../../assets/icons/flexao-4-pontos.png")
        div.style.display = 'flex'
        document.querySelector('#Lshear').focus()
    } else {
        img.setAttribute('src', "../../assets/icons/flexao-3-pontos.png")
        div.style.display = 'none'
    }
}

function setLoadCondition() {
    if (radioButton[0].checked && document.querySelector('#Lshear').value == '') {
        ipcRenderer.send('create-dialog', {title: window.i18n.__('Fill in all fields.'), description: ''})
        document.querySelector('#Lshear').focus()
        return
    }
    var model = readData('model.json')
    model.loadType.bending = true
    model.loadType.normal = false
    if (radioButton[0].checked) {
        const Lshear = parseFloat(document.querySelector('#Lshear').value.replace(',', '.'))
        if (model.sectionProperties.L && Lshear >= model.sectionProperties.L/2) {
            ipcRenderer.send('create-dialog', {title: 'Erro', description: 'O Lshear deve ser menor que a metade de L.'})
            return
        }
        model.loadProperties = {
            points: 4,
            Lshear: Lshear
        }
    } else {
        model.loadProperties = {
            points: 3
        }
    }

    writeData(model, 'model.json')
    var inputStatus = JSON.parse(localStorage.getItem('input-status'))
    inputStatus.load = true
    localStorage.setItem('input-status', JSON.stringify(inputStatus))
    ipcRenderer.send('delete-current-window')
}

function cancel() {
    ipcRenderer.send('delete-current-window')
}