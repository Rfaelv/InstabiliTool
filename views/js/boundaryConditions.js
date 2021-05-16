const { ipcRenderer, dialog } = require('electron')
const {readData, writeData} = require('../../modules/writeAndReadData')

var model = readData('model.json')
createDOM()

const applybutton = document.getElementById('apply')
applybutton.addEventListener('click', setBoundaryConditions)

const cancelbutton = document.getElementById('cancel')
cancelbutton.addEventListener('click', cancel)

function createDOM() {
    var img = document.getElementById('img')
    var table1 = document.getElementById('1')
    var table2 = document.getElementById('2')
    var table3 = document.getElementById('3')

    if (model.sectionType.I) {
        img.src = '../../assets/icons/vigaI-explodido.png'
        table3.style.display = 'block'

        var lastCheckbox1 = document.getElementsByClassName('checkbox3-1')[6]
        var lastCheckbox2 = document.getElementsByClassName('checkbox3-2')[6]
        var lastCheckbox3 = document.getElementsByClassName('checkbox3-3')[6]

        lastCheckbox1.addEventListener('change', changeAll31)
        lastCheckbox2.addEventListener('change', changeAll32)
        lastCheckbox3.addEventListener('change', changeAll33)

    } else if (model.sectionType.tubular) {
        img.src = '../../assets/icons/vigaTubular-explodido.png'
        table2.style.display = 'block'

        var lastCheckbox1 = document.getElementsByClassName('checkbox2-1')[6]
        var lastCheckbox2 = document.getElementsByClassName('checkbox2-2')[6]

        lastCheckbox1.addEventListener('change', changeAll21)
        lastCheckbox2.addEventListener('change', changeAll22)

    } else if (model.sectionType.C) {
        img.src = '../../assets/icons/vigaC-explodido.png'
        table3.style.display = 'block'

        var lastCheckbox1 = document.getElementsByClassName('checkbox3-1')[6]
        var lastCheckbox2 = document.getElementsByClassName('checkbox3-2')[6]
        var lastCheckbox3 = document.getElementsByClassName('checkbox3-3')[6]

        lastCheckbox1.addEventListener('change', changeAll31)
        lastCheckbox2.addEventListener('change', changeAll32)
        lastCheckbox3.addEventListener('change', changeAll33)

    } else if (model.sectionType.C2) {
        img.src = '../../assets/icons/vigaC2-explodido.png'
        table3.style.display = 'block'

        var lastCheckbox1 = document.getElementsByClassName('checkbox3-1')[6]
        var lastCheckbox2 = document.getElementsByClassName('checkbox3-2')[6]
        var lastCheckbox3 = document.getElementsByClassName('checkbox3-3')[6]

        lastCheckbox1.addEventListener('change', changeAll31)
        lastCheckbox2.addEventListener('change', changeAll32)
        lastCheckbox3.addEventListener('change', changeAll33)

    } else if (model.sectionType.rack) {
        img.src = '../../assets/icons/vigaRack-explodido.png'
        table3.style.display = 'block'

        var lastCheckbox1 = document.getElementsByClassName('checkbox3-1')[6]
        var lastCheckbox2 = document.getElementsByClassName('checkbox3-2')[6]
        var lastCheckbox3 = document.getElementsByClassName('checkbox3-3')[6]

        lastCheckbox1.addEventListener('change', changeAll31)
        lastCheckbox2.addEventListener('change', changeAll32)
        lastCheckbox3.addEventListener('change', changeAll33)

    } else if (model.sectionType.angle) {
        img.src = '../../assets/icons/cantoneira-explodido.png'
        table2.style.display = 'block'

        var lastCheckbox1 = document.getElementsByClassName('checkbox2-1')[6]
        var lastCheckbox2 = document.getElementsByClassName('checkbox2-2')[6]

        lastCheckbox1.addEventListener('change', changeAll21)
        lastCheckbox2.addEventListener('change', changeAll22)

    } else if (model.sectionType.plate) {
        img.src = '../../assets/icons/plate-hover2.png'
        table1.style.display = 'block'

        var lastCheckbox1 = document.getElementsByClassName('checkbox1-1')[6]

        lastCheckbox1.addEventListener('change', changeAll11)

    }
}

function setBoundaryConditions() {
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

function cancel() {
    ipcRenderer.send('delete-current-window')
}

function apply3() {
    var checkbox1 = document.getElementsByClassName('checkbox3-1')
        var checkbox2 = document.getElementsByClassName('checkbox3-2')
        var checkbox3 = document.getElementsByClassName('checkbox3-3')

        var boundaryConditions = [
            {
                UX: true,
                UY: true,
                UZ: true,
                ROTX: true,
                ROTY: true,
                ROTZ: true
            },
            {
                UX: true,
                UY: true,
                UZ: true,
                ROTX: true,
                ROTY: true,
                ROTZ: true
            },
            {
                UX: true,
                UY: true,
                UZ: true,
                ROTX: true,
                ROTY: true,
                ROTZ: true
            }
        ]
        var cont = 0
        for (var key in boundaryConditions[0]) {
            boundaryConditions[0][key] = checkbox1[cont].checked
            boundaryConditions[1][key] = checkbox2[cont].checked
            boundaryConditions[2][key] = checkbox3[cont].checked
            cont += 1
        }
        model.boundaryConditions = boundaryConditions
        writeData(model, 'model.json')
        ipcRenderer.send('delete-current-window')
}

function apply2() {
    var checkbox1 = document.getElementsByClassName('checkbox2-1')
    var checkbox2 = document.getElementsByClassName('checkbox2-2')

    var boundaryConditions = [
        {
            UX: true,
            UY: true,
            UZ: true,
            ROTX: true,
            ROTY: true,
            ROTZ: true
        },
        {
            UX: true,
            UY: true,
            UZ: true,
            ROTX: true,
            ROTY: true,
            ROTZ: true
        }
    ]
    var cont = 0
    for (var key in boundaryConditions[0]) {
        boundaryConditions[0][key] = checkbox1[cont].checked
        boundaryConditions[1][key] = checkbox2[cont].checked
        cont += 1
    }
    model.boundaryConditions = boundaryConditions
    writeData(model, 'model.json')
    ipcRenderer.send('delete-current-window')
}

function apply1() {
    var checkbox1 = document.getElementsByClassName('checkbox1-1')

    var boundaryConditions = [
        {
            UX: true,
            UY: true,
            UZ: true,
            ROTX: true,
            ROTY: true,
            ROTZ: true
        }
    ]
    var cont = 0
    for (var key in boundaryConditions[0]) {
        boundaryConditions[0][key] = checkbox1[cont].checked
        cont += 1
    }
    model.boundaryConditions = boundaryConditions
    writeData(model, 'model.json')
    ipcRenderer.send('delete-current-window')
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