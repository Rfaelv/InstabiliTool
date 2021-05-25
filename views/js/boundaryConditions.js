const { ipcRenderer, dialog } = require('electron')
const fs = require('fs')
const readXlsxFile = require('read-excel-file/node')
const {readData, writeData} = require('../../modules/writeAndReadData')

var model = readData('model.json')
createDOM()

const applybutton = document.getElementById('apply')
applybutton.addEventListener('click', setBoundaryConditions)

const cancelbutton = document.getElementById('cancel')
cancelbutton.addEventListener('click', cancel)

document.getElementById('searchButton')
    .addEventListener('click', searchTable)

document.getElementById('downloadButton')
    .addEventListener('click', downloadExampleTable)

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
            ipcRenderer.send('delete-current-window')
        })
    } else {
        model.boundaryConditions.table = ''
        writeData(model, 'model.json')
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

    var boundaryConditions = {
        personalized: true,
        1: {
            UX: true,
            UY: true,
            UZ: true,
            ROTX: true,
            ROTY: true,
            ROTZ: true
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
        cont += 1
    }
    model.boundaryConditions = boundaryConditions
}

function apply2() {
    var checkbox1 = document.getElementsByClassName('checkbox2-1')
    var checkbox2 = document.getElementsByClassName('checkbox2-2')

    var boundaryConditions = {
        personalized: true,
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
        cont += 1
    }
    model.boundaryConditions = boundaryConditions
}

function apply1() {
    var checkbox1 = document.getElementsByClassName('checkbox1-1')

    var boundaryConditions = {
        personalized: true,
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
        cont += 1
    }
    model.boundaryConditions = boundaryConditions
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
        title:'Salvar Planilha',
        properties: ['openDirectory'],
        defaultPath: 'Boundary-conditions-sheet',
        filters: [
            { name: 'planilha do excel', extensions: ['xlsx', 'xls'] },
        ]
    }).then(result => {
        if (result.filePath) {
            fs.copyFileSync('data/example-sheet.xlsx', result.filePath)  
        } 
    })
}

function searchTable() {
    const { dialog } = require('electron').remote
    dialog.showOpenDialog({
        title:'Selecionar tabela',
        properties: ['openFile'],
        filters: [
            { name: 'planilha do excel', extensions: ['xlsm', 'xlsx'] },
          ]
    }).then(result => {
        const textBox = document.getElementById('tablePath')
        textBox.value = result.filePaths.length == 0? textBox.value : result.filePaths       
    })
}