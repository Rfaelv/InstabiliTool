const { ipcRenderer, dialog } = require('electron')
const fs = require('fs')
const path = require('path')
const readXlsxFile = require('read-excel-file/node')
const { exec } = require('child_process')
const {readData, writeData} = require('../../modules/writeAndReadData')

var model = readData('model.json')
createDOM()
localStorage.setItem("boundary-consition-data", "[]")

var zIndex = 0

window.addEventListener("close", () => {localStorage.setItem("boundary-consition-data", "[]")})

const applybutton = document.getElementById('apply')
applybutton.addEventListener('click', setBoundaryConditions)

const cancelbutton = document.getElementById('cancel')
cancelbutton.addEventListener('click', cancel)

document.getElementById("previous")
    .addEventListener("click", previousZPosition)

document.getElementById("next")
    .addEventListener("click", nextZPosition)

document.getElementById('searchButton')
    .addEventListener('click', searchTable)

document.getElementById('downloadButton')
    .addEventListener('click', downloadExampleTable)

document.getElementById('current-position').focus()

function createDOM() {
    var img = document.getElementById('img')
    var img2 = document.getElementById('img2')
    // var axes = document.getElementById('axes')
    // title="<span><img id='img2' height='280px'></span>">
    var table1 = document.getElementById('1')
    var table2 = document.getElementById('2')
    var table3 = document.getElementById('3')

    if (model.sectionType.I) {
        img.src = '../../assets/icons/vigaI-explodido.png'
        img2.src = '../../assets/icons/vigaI-axes.png'
        table3.style.display = 'block'

        var lastCheckbox1 = document.getElementsByClassName('checkbox3-1')[6]
        var lastCheckbox2 = document.getElementsByClassName('checkbox3-2')[6]
        var lastCheckbox3 = document.getElementsByClassName('checkbox3-3')[6]

        lastCheckbox1.addEventListener('change', changeAll31)
        lastCheckbox2.addEventListener('change', changeAll32)
        lastCheckbox3.addEventListener('change', changeAll33)

    } else if (model.sectionType.tubular) {
        img.src = '../../assets/icons/vigaTubular-explodido.png'
        img2.src = '../../assets/icons/vigaTubular-axes.png'
        table2.style.display = 'block'

        var lastCheckbox1 = document.getElementsByClassName('checkbox2-1')[6]
        var lastCheckbox2 = document.getElementsByClassName('checkbox2-2')[6]

        lastCheckbox1.addEventListener('change', changeAll21)
        lastCheckbox2.addEventListener('change', changeAll22)

    } else if (model.sectionType.C) {
        img.src = '../../assets/icons/vigaC-explodido.png'
        img2.src = '../../assets/icons/vigaC-axes.png'
        table3.style.display = 'block'

        var lastCheckbox1 = document.getElementsByClassName('checkbox3-1')[6]
        var lastCheckbox2 = document.getElementsByClassName('checkbox3-2')[6]
        var lastCheckbox3 = document.getElementsByClassName('checkbox3-3')[6]

        lastCheckbox1.addEventListener('change', changeAll31)
        lastCheckbox2.addEventListener('change', changeAll32)
        lastCheckbox3.addEventListener('change', changeAll33)

    } else if (model.sectionType.C2) {
        img.src = '../../assets/icons/vigaC2-explodido.png'
        img2.src = '../../assets/icons/vigaC2-axes.png'
        table3.style.display = 'block'

        var lastCheckbox1 = document.getElementsByClassName('checkbox3-1')[6]
        var lastCheckbox2 = document.getElementsByClassName('checkbox3-2')[6]
        var lastCheckbox3 = document.getElementsByClassName('checkbox3-3')[6]

        lastCheckbox1.addEventListener('change', changeAll31)
        lastCheckbox2.addEventListener('change', changeAll32)
        lastCheckbox3.addEventListener('change', changeAll33)

    } else if (model.sectionType.rack) {
        img.src = '../../assets/icons/vigaRack-explodido.png'
        // axes.title = "<img src='../../assets/icons/vigaRack-axes.png' height='280px'>"
        // i = document.createElement('img')
        // i.src = '../../assets/icons/vigaRack-axes.png'
        // // axes.title = i
        img2.src = '../../assets/icons/vigaRack-axes.png'
        table3.style.display = 'block'

        var lastCheckbox1 = document.getElementsByClassName('checkbox3-1')[6]
        var lastCheckbox2 = document.getElementsByClassName('checkbox3-2')[6]
        var lastCheckbox3 = document.getElementsByClassName('checkbox3-3')[6]

        lastCheckbox1.addEventListener('change', changeAll31)
        lastCheckbox2.addEventListener('change', changeAll32)
        lastCheckbox3.addEventListener('change', changeAll33)

    } else if (model.sectionType.angle) {
        img.src = '../../assets/icons/cantoneira-explodido.png'
        img2.src = '../../assets/icons/cantoneira-axes.png'
        table2.style.display = 'block'

        var lastCheckbox1 = document.getElementsByClassName('checkbox2-1')[6]
        var lastCheckbox2 = document.getElementsByClassName('checkbox2-2')[6]

        lastCheckbox1.addEventListener('change', changeAll21)
        lastCheckbox2.addEventListener('change', changeAll22)

    } else if (model.sectionType.plate) {
        img.src = '../../assets/icons/plate-hover2.png'
        img2.src = '../../assets/icons/plate-axes.png'
        table1.style.display = 'block'

        var lastCheckbox1 = document.getElementsByClassName('checkbox1-1')[6]

        lastCheckbox1.addEventListener('change', changeAll11)

    }
}

function setBoundaryConditions() {
    localStorage.setItem('personalized-boundary-conditions', 'y')

    if (zIndex === JSON.parse(localStorage.getItem("boundary-consition-data")).length) {
        setData()
    }

    model.boundaryConditions.personalized = true
    model.boundaryConditions.data = JSON.parse(localStorage.getItem("boundary-consition-data"))

    const tablePath = document.getElementById('tablePath').value

    if (tablePath != '') {
        readXlsxFile(tablePath).then((rows) => {
            model.boundaryConditions.table = rows
        }).catch((error) => {
            if (error.errno == -4058) {
                ipcRenderer.send('create-dialog', {title: `${window.i18n.__('Cannot open')} ${error.path}`, description: ''})
            } else {
                ipcRenderer.send('create-dialog', {title: window.i18n.__('Cannot open the file'), description: ''})
            }
        }).finally(() => {
            writeData(model, 'model.json')
            var inputStatus = JSON.parse(localStorage.getItem('input-status'))
            inputStatus.bd = true
            localStorage.setItem('input-status', JSON.stringify(inputStatus))
            ipcRenderer.send('delete-current-window')
        })
    } else {
        model.boundaryConditions.table = ''
        writeData(model, 'model.json')
        var inputStatus = JSON.parse(localStorage.getItem('input-status'))
        inputStatus.bd = true
        localStorage.setItem('input-status', JSON.stringify(inputStatus))
        ipcRenderer.send('delete-current-window')
    }
}

function cancel() {
    ipcRenderer.send('delete-current-window')
}

function apply3() {
    var checkbox1 = document.getElementsByClassName('checkbox3-1')
    var checkbox2 = document.getElementsByClassName('checkbox3-2')
    var checkbox3 = document.getElementsByClassName('checkbox3-3')
    var zInput = document.getElementById("current-position").value
    const z = parseFloat(zInput.replace(',', '.'))

    var boundaryConditions = {
        z: z,
        1: {
            UX: true,
            UY: true,
            UZ: true,
            ROTX: true,
            ROTY: true,
            ROTZ: true,
            all: true
        },
        2: {
            UX: true,
            UY: true,
            UZ: true,
            ROTX: true,
            ROTY: true,
            ROTZ: true
        },
        3: {
            UX: true,
            UY: true,
            UZ: true,
            ROTX: true,
            ROTY: true,
            ROTZ: true
        }
    }
    var cont = 0

    for (var key in boundaryConditions['1']) {
        boundaryConditions['1'][key] = checkbox1[cont].checked
        boundaryConditions['2'][key] = checkbox2[cont].checked
        boundaryConditions['3'][key] = checkbox3[cont].checked

        checkbox1[cont].checked = false
        checkbox2[cont].checked = false
        checkbox3[cont].checked = false

        cont += 1
    }
    document.getElementById("current-position").value = ""
    document.getElementById("current-position").focus()

    var boundaryConditionsData = JSON.parse(localStorage.getItem("boundary-consition-data"))

    if (zIndex < boundaryConditionsData.length) {
        boundaryConditionsData.splice(zIndex, 1, boundaryConditions)
    } else {
        boundaryConditionsData.push(boundaryConditions)
    }

    localStorage.setItem("boundary-consition-data", JSON.stringify(boundaryConditionsData))
}

function get3() {
    var checkbox1 = document.getElementsByClassName('checkbox3-1')
    var checkbox2 = document.getElementsByClassName('checkbox3-2')
    var checkbox3 = document.getElementsByClassName('checkbox3-3')
    var boundaryConditionsData = JSON.parse(localStorage.getItem("boundary-consition-data"))[zIndex]

    var cont = 0

    for (var key in boundaryConditionsData["1"]) {
        checkbox1[cont].checked = boundaryConditionsData["1"][key]
        checkbox2[cont].checked = boundaryConditionsData["2"][key]
        checkbox3[cont].checked = boundaryConditionsData["3"][key]
        cont += 1
    }
    document.getElementById("current-position").value = boundaryConditionsData.z
}

function apply2() {
    var checkbox1 = document.getElementsByClassName('checkbox2-1')
    var checkbox2 = document.getElementsByClassName('checkbox2-2')
    const z = parseFloat(document.getElementById("current-position").value.replace(',', '.'))

    var boundaryConditions = {
        z: z,
        1:{
            UX: true,
            UY: true,
            UZ: true,
            ROTX: true,
            ROTY: true,
            ROTZ: true
        },
        2:{
            UX: true,
            UY: true,
            UZ: true,
            ROTX: true,
            ROTY: true,
            ROTZ: true
        }
    }
    var cont = 0

    for (var key in boundaryConditions[0]) {
        boundaryConditions[0][key] = checkbox1[cont].checked
        boundaryConditions[1][key] = checkbox2[cont].checked

        checkbox1[cont].checked = false
        checkbox2[cont].checked = false

        cont += 1
    }
    document.getElementById("current-position").value = ""
    document.getElementById("current-position").focus()

    var boundaryConditionsData = JSON.parse(localStorage.getItem("boundary-consition-data"))

    if (zIndex < boundaryConditionsData.length) {
        boundaryConditionsData.splice(zIndex, 1, boundaryConditions)
    } else {
        boundaryConditionsData.push(boundaryConditions)
    }

    localStorage.setItem("boundary-consition-data", JSON.stringify(boundaryConditionsData))
}

function get2() {
    var checkbox1 = document.getElementsByClassName('checkbox2-1')
    var checkbox2 = document.getElementsByClassName('checkbox2-2')
    var boundaryConditionsData = JSON.parse(localStorage.getItem("boundary-consition-data"))[zIndex]

    var cont = 0

    for (var key in boundaryConditionsData["1"]) {
        checkbox1[cont].checked = boundaryConditionsData["1"][key]
        checkbox2[cont].checked = boundaryConditionsData["2"][key]
        cont += 1
    }
    document.getElementById("current-position").value = boundaryConditionsData.z
}

function apply1() {
    var checkbox1 = document.getElementsByClassName('checkbox1-1')
    const z = parseFloat(document.getElementById("current-position").value.replace(',', '.'))

    var boundaryConditions = {
        z: z,
        1:{
            UX: true,
            UY: true,
            UZ: true,
            ROTX: true,
            ROTY: true,
            ROTZ: true
        }
    }
    var cont = 0

    for (var key in boundaryConditions[0]) {
        boundaryConditions[0][key] = checkbox1[cont].checked

        checkbox1[cont].checked = false
        
        cont += 1
    }
    document.getElementById("current-position").value = ""
    document.getElementById("current-position").focus()

    var boundaryConditionsData = JSON.parse(localStorage.getItem("boundary-consition-data"))
    
    if (zIndex < boundaryConditionsData.length) {
        boundaryConditionsData.splice(zIndex, 1, boundaryConditions)
    } else {
        boundaryConditionsData.push(boundaryConditions)
    }

    localStorage.setItem("boundary-consition-data", JSON.stringify(boundaryConditionsData))
}

function get1() {
    var checkbox1 = document.getElementsByClassName('checkbox1-1')
    var boundaryConditionsData = JSON.parse(localStorage.getItem("boundary-consition-data"))[zIndex]

    var cont = 0

    for (var key in boundaryConditionsData["1"]) {
        checkbox1[cont].checked = boundaryConditionsData["1"][key]
        cont += 1
    }
    document.getElementById("current-position").value = boundaryConditionsData.z
}

function changeAll31() {
    var checkbox1 = document.getElementsByClassName('checkbox3-1')
    if (checkbox1[6].checked) {
        for (input of checkbox1) {
            input.checked = true
        }
    } else {
        for (input of checkbox1) {
            input.checked = false
        }
    }  
}

function changeAll32() {
    var checkbox1 = document.getElementsByClassName('checkbox3-2')
    if (checkbox1[6].checked) {
        for (input of checkbox1) {
            input.checked = true
        }
    } else {
        for (input of checkbox1) {
            input.checked = false
        }
    }  
}

function changeAll33() {
    var checkbox1 = document.getElementsByClassName('checkbox3-3')
    if (checkbox1[6].checked) {
        for (input of checkbox1) {
            input.checked = true
        }
    } else {
        for (input of checkbox1) {
            input.checked = false
        }
    }  
}

function changeAll21() {
    var checkbox1 = document.getElementsByClassName('checkbox2-1')
    if (checkbox1[6].checked) {
        for (input of checkbox1) {
            input.checked = true
        }
    } else {
        for (input of checkbox1) {
            input.checked = false
        }
    }  
}

function changeAll22() {
    var checkbox1 = document.getElementsByClassName('checkbox2-2')
    if (checkbox1[6].checked) {
        for (input of checkbox1) {
            input.checked = true
        }
    } else {
        for (input of checkbox1) {
            input.checked = false
        }
    }  
}

function changeAll11() {
    var checkbox1 = document.getElementsByClassName('checkbox1-1')
    if (checkbox1[6].checked) {
        for (input of checkbox1) {
            input.checked = true
        }
    } else {
        for (input of checkbox1) {
            input.checked = false
        }
    }  
}

function downloadExampleTable() {
    const { dialog } = require('electron').remote
    dialog.showSaveDialog({
        title: window.i18n.__('Save Spreadsheet'),
        properties: ['openDirectory'],
        defaultPath: window.i18n.__('Boundary-conditions-sheet'),
        filters: [
            { name: window.i18n.__('excel spreadsheet'), extensions: ['xlsx', 'xls'] },
        ]
    }).then(result => {
        if (result.filePath) {
            fs.copyFileSync(`data/${window.i18n.__('example-sheet')}.xlsx`, result.filePath)
            exec(result.filePath, (error, stdout, stderr) => {
                if (error) {
                    console.log(`error: ${error.message}`)
                    return
                }
                if (stderr) {
                    console.log(`stderr: ${stderr}`)
                }
            })
        } 
    })
}

function searchTable() {
    const { dialog } = require('electron').remote
    dialog.showOpenDialog({
        title: window.i18n.__('Select Table'),
        properties: ['openFile'],
        filters: [
            { name: window.i18n.__('excel spreadsheet'), extensions: ['xlsm', 'xlsx'] },
          ]
    }).then(result => {
        const textBox = document.getElementById('tablePath')
        textBox.value = result.filePaths.length == 0? textBox.value : result.filePaths       
    })
}

function previousZPosition() {
    const zinput = document.getElementById("current-position").value

    if ( zinput === "") {
        ipcRenderer.send('create-dialog', {title: window.i18n.__('Fill in the z position field.'), description: ''})
        return
    }

    if (zIndex >= 1) {
        setData()
        zIndex -= 1
        getData()
    }
}

function nextZPosition() {
    const zinput = document.getElementById("current-position").value
    
    if ( zinput === "") {
        ipcRenderer.send('create-dialog', {title: window.i18n.__('Fill in the z position field.'), description: ''})
    } else {
        const boundaryDataLength = JSON.parse(localStorage.getItem("boundary-consition-data")).length

        if (zIndex >= boundaryDataLength - 1) {
            setData()
            zIndex += 1
        } else {
            setData()
            zIndex += 1
            getData()
        }
    }
}

function setData() {
    if (model.sectionType.I) {
        apply3()

    } else if (model.sectionType.tubular) {
        apply2()

    } else if (model.sectionType.C) {
        apply3()

    } else if (model.sectionType.C2) {
        apply3()

    } else if (model.sectionType.rack) {
        apply3()

    } else if (model.sectionType.angle) {
        apply2()

    } else if (model.sectionType.plate) {
        apply1()

    }
}

function getData() {
    if (model.sectionType.I) {
        get3()

    } else if (model.sectionType.tubular) {
        get2()

    } else if (model.sectionType.C) {
        get3()

    } else if (model.sectionType.C2) {
        get3()

    } else if (model.sectionType.rack) {
        get3()

    } else if (model.sectionType.angle) {
        get2()

    } else if (model.sectionType.plate) {
        get1()

    }
}