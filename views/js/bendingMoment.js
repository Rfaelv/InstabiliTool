const { ipcRenderer } = require('electron')
const {writeData, readData} = require('../../modules/writeAndReadData')

document.querySelector('#Lshear').focus()

createDOM()

const radioButton = document.getElementsByName('flexao')
radioButton[0].addEventListener('change', switchImage)
radioButton[1].addEventListener('change', switchImage)
radioButton[2].addEventListener('change', switchImage)

const radioButton2 = document.getElementsByName('direction')

const applybutton = document.getElementById('apply')
applybutton.addEventListener('click', setLoadCondition)

const cancelbutton = document.getElementById('cancel')
cancelbutton.addEventListener('click', cancel)

window.addEventListener('load', () => {
    setModelData()
})


function switchImage() {
    var img = document.getElementById('image-flexao')
    var div1 = document.getElementById('input1') 
    var div2 = document.getElementById('input2') 
    var label = document.getElementById('direction')

    if (radioButton[0].checked) {
        div2.style.display = 'none'
        label.style.display = 'none'
        img.style.display = 'flex'
        img.setAttribute('src', "../../assets/icons/flexao-4-pontos.png")
        div1.style.display = 'flex'
        document.querySelector('#Lshear').focus()
    } else if (radioButton[1].checked){
        div2.style.display = 'none'
        label.style.display = 'none'
        img.style.display = 'flex'
        img.setAttribute('src', "../../assets/icons/flexao-3-pontos.png")
        div1.style.display = 'none'
    } else {
        img.style.display = 'none'
        div1.style.display = 'none'
        div2.style.display = 'flex'
        label.style.display = 'flex'
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
    } else if (radioButton[1].checked) {
        model.loadProperties = {
            points: 3
        }
    } else {
        model.loadProperties = {
            direction: radioButton2[0].checked ? 'x' : 'y'
        }
    }

    writeData(model, 'model.json')
    // var inputStatus = JSON.parse(localStorage.getItem('input-status'))
    // inputStatus.load = true
    // localStorage.setItem('input-status', JSON.stringify(inputStatus))
    ipcRenderer.send('delete-current-window')
}

function cancel() {
    ipcRenderer.send('delete-current-window')
}

function setModelData() {
    const model = readData('model.json')

    if (model.loadProperties.points == 3) {
        document.getElementsByName('flexao')[1].checked = true
        switchImage()
        
    } else if (model.loadProperties.points == 4) {
        document.getElementById('Lshear').value = model.loadProperties.Lshear
        switchImage()

    } else if (model.loadProperties.direction) {
        document.getElementsByName('flexao')[2].checked = true
        if (model.loadProperties.direction == 'x') {
            document.getElementsByName('direction')[0].checked = true
        } else {
            document.getElementsByName('direction')[1].checked = true
        }
        switchImage()
    }
}

function createDOM() {
    const model = readData('model.json')
    const img2 = document.getElementById('img2')

    if (model.sectionType.I) {
        img2.src = '../../assets/icons/vigaI-axes.png'

    } else if (model.sectionType.tubular) {
        img2.src = '../../assets/icons/vigaTubular-axes.png'

    } else if (model.sectionType.C) {
        img2.src = '../../assets/icons/vigaC-axes.png'

    } else if (model.sectionType.C2) {

        img2.src = '../../assets/icons/vigaC2-axes.png'

    } else if (model.sectionType.rack) {
        img2.src = '../../assets/icons/vigaRack-axes.png'

    } else if (model.sectionType.angle) {
        img2.src = '../../assets/icons/cantoneira-axes.png'

    } else if (model.sectionType.plate) {
        img2.src = '../../assets/icons/plate-axes.png'
    }
}