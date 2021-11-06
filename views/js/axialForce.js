const { ipcRenderer } = require('electron')
const {writeData, readData} = require('../../modules/writeAndReadData')

document.querySelector('#x').focus()

createDOM()

const applybutton = document.getElementById('apply')
applybutton.addEventListener('click', setLoadCondition)

const cancelbutton = document.getElementById('cancel')
cancelbutton.addEventListener('click', cancel)

const radio = document.getElementsByName("axial-force")
radio.forEach(() => {
    this.addEventListener('change', changeInput)
}) 

window.addEventListener('load', () => {
    setModelData()
})

function setLoadCondition() {
    const x = document.getElementById('x')
    const y = document.getElementById('y')

    var model = readData('model.json')
    model.loadType.normal = true
    model.loadType.bending = false

    if (radio[0].checked) {
        model.loadProperties = {
            type: "point",
            x: parseFloat(x.value === "" ? 0 : x.value.replace(',', '.')),
            y: parseFloat(y.value === "" ? 0 : y.value.replace(',', '.'))
        }
    } else {
        model.loadProperties = {
            type: "distributed"
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

function changeInput(event) {
    if (document.getElementsByName("axial-force")[0].checked) {
        document.getElementById("divinput").style.display = "flex"
        document.getElementById("divtext").style.display = "none"
        document.getElementById("x").focus()
    } else {
        document.getElementById("divinput").style.display = "none"
        document.getElementById("divtext").style.display = "flex"
    }
}

function setModelData() {
    const model = readData('model.json')

    if (model.loadProperties.type == 'point') {
        document.getElementsByName('axial-force')[0].checked = true
        document.getElementById('x').value = model.loadProperties.x
        document.getElementById('y').value = model.loadProperties.y
        
    } else if (model.loadProperties.type == 'distributed') {
        document.getElementsByName('axial-force')[1].checked = true
        changeInput()
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