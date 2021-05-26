const { ipcRenderer, dialog } = require('electron')
const {readData, writeData} = require('../../modules/writeAndReadData')
const fs = require('fs')
const path = require('path')

configMaterialInput()

// $(document).ready(function () {
//     $('[data-toggle="tooltip"]').tooltip({ boundary: 'window' });
// })

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.tooltipped');
    var instances = M.Tooltip.init(elems, options);
});

const applybutton = document.getElementById('apply')
applybutton.addEventListener('click', setMeshAndMaterialAssignment)

const cancelbutton = document.getElementById('cancel')
cancelbutton.addEventListener('click', cancel)

const vizualizerButton = document.getElementById('visualizeButton')
vizualizerButton.addEventListener('click', openMeshVisualizer)

vizualizerButton.title = window.i18n.__('View mesh')

document.getElementById('elementSize').focus()


function setMeshAndMaterialAssignment() {
    const elementSize = document.getElementById('elementSize')
    const elementMethod = document.getElementsByName('method')
    const selects = document.getElementsByClassName('materialAssignment')

    if (elementSize.value == '' || (!elementMethod[0].checked && !elementMethod[1].checked)) {
        ipcRenderer.send('create-dialog', {title: window.i18n.__('Fill in all fields.'), description: ''})
        if (elementSize.value == '') {
            elementSize.focus()
        }
        return
    }

    var model = readData('model.json')
    model.meshProperties.elementSize = parseFloat(elementSize.value.replace(',', '.'))
    model.meshProperties.method = parseFloat((elementMethod[0].checked? 0 : 1))

    var materialAssignmentList = []
    for (select of selects) {
        materialAssignmentList.push(parseInt(select.options[select.selectedIndex].value))
    }
    model.sectionProperties.materialAssignment = materialAssignmentList.length == 0 ? [1,1,1] : materialAssignmentList
    writeData(model, 'model.json')
    var inputStatus = JSON.parse(localStorage.getItem('input-status'))
    inputStatus.mesh = true
    localStorage.setItem('input-status', JSON.stringify(inputStatus))
    ipcRenderer.send('delete-current-window')
}


function cancel() {
    ipcRenderer.send('delete-current-window')
}

function configMaterialInput() {
    var div = document.getElementById('addMateial')
    const model = readData('model.json')

    if(model.materials.length == 0) {
        var paragraph = document.createElement('p')
        const text = document.createTextNode(window.i18n.__('Create at least one material to add to profile.'))
        paragraph.appendChild(text)
        div.appendChild(paragraph)
    } else if(model.materials.length == 1) {
        var paragraph = document.createElement('p')
        const text = document.createTextNode(`${model.materials[0].tag} ${window.i18n.__('will be used for whole profile. To use more then one material in the profile, create others materials and come back to here.')}`)
        paragraph.appendChild(text)
        div.appendChild(paragraph)

    } else {
        if (model.sectionType.I) {
            const divImg = document.createElement('div')
            divImg.setAttribute('id', 'img')
            const img = document.createElement('img')
            img.setAttribute('src', '../../assets/icons/vigaI-explodido.png')
            img.setAttribute('height', '120px')
            const inputDiv = document.createElement('div')
            inputDiv.setAttribute('id', 'inputDiv')
            const div1 = document.createElement('div')
            const div2 = document.createElement('div')
            const div3 = document.createElement('div')
            const label1 = document.createElement('label')
            const label2 = document.createElement('label')
            const label3 = document.createElement('label')
            const textLabel1 = document.createTextNode('1')
            const textLabel2 = document.createTextNode('2')
            const textLabel3 = document.createTextNode('3')
            const select1 = document.createElement('select')
            const select2= document.createElement('select')
            const select3 = document.createElement('select')
            select1.setAttribute('class', 'materialAssignment')
            select2.setAttribute('class', 'materialAssignment')
            select3.setAttribute('class', 'materialAssignment')

            for (let i = 0; i < model.materials.length; i++) {
                var opt1 = document.createElement("option")
                // opt1.value = model.materials[i].tag
                opt1.value = i + 1
                opt1.text = model.materials[i].tag
                var opt2 = document.createElement("option")
                // opt2.value = model.materials[i].tag
                opt2.value = i + 1
                opt2.text = model.materials[i].tag
                var opt3 = document.createElement("option")
                // opt3.value = model.materials[i].tag
                opt3.value = i + 1
                opt3.text = model.materials[i].tag
                select1.add(opt1, select1.options[i])
                select2.add(opt2, select2.options[i])
                select3.add(opt3, select3.options[i])
            }
            divImg.appendChild(img)

            label1.appendChild(textLabel1)
            label2.appendChild(textLabel2)
            label3.appendChild(textLabel3)

            div1.appendChild(label1)
            div1.appendChild(select1)
            div2.appendChild(label2)
            div2.appendChild(select2)
            div3.appendChild(label3)
            div3.appendChild(select3)

            inputDiv.appendChild(div1)
            inputDiv.appendChild(div2)
            inputDiv.appendChild(div3)

            div.appendChild(divImg)
            div.appendChild(inputDiv)

        } else if (model.sectionType.tubular) {
            const divImg = document.createElement('div')
            divImg.setAttribute('id', 'img')
            const img = document.createElement('img')
            img.setAttribute('src', '../../assets/icons/vigaTubular-explodido.png')
            img.setAttribute('height', '120px')
            const inputDiv = document.createElement('div')
            inputDiv.setAttribute('id', 'inputDiv')
            const div1 = document.createElement('div')
            const div2 = document.createElement('div')
            const label1 = document.createElement('label')
            const label2 = document.createElement('label')
            const textLabel1 = document.createTextNode('1')
            const textLabel2 = document.createTextNode('2')
            const select1 = document.createElement('select')
            const select2= document.createElement('select')
            select1.setAttribute('className', 'materialAssignment')
            select2.setAttribute('className', 'materialAssignment')

            for (let i in model.materials) {
                var opt1 = document.createElement("option")
                opt1.value = model.materials[i].tag
                opt1.text = model.materials[i].tag
                var opt2 = document.createElement("option")
                opt2.value = model.materials[i].tag
                opt2.text = model.materials[i].tag
                select1.add(opt1, select1.options[i])
                select2.add(opt2, select2.options[i])
            }
            divImg.appendChild(img)

            label1.appendChild(textLabel1)
            label2.appendChild(textLabel2)

            div1.appendChild(label1)
            div1.appendChild(select1)
            div2.appendChild(label2)
            div2.appendChild(select2)

            inputDiv.appendChild(div1)
            inputDiv.appendChild(div2)

            div.appendChild(divImg)
            div.appendChild(inputDiv)

        } else if (model.sectionType.C) {
            const divImg = document.createElement('div')
            divImg.setAttribute('id', 'img')
            const img = document.createElement('img')
            img.setAttribute('src', '../../assets/icons/vigaC-explodido.png')
            img.setAttribute('height', '120px')
            const inputDiv = document.createElement('div')
            inputDiv.setAttribute('id', 'inputDiv')
            const div1 = document.createElement('div')
            const div2 = document.createElement('div')
            const div3 = document.createElement('div')
            const label1 = document.createElement('label')
            const label2 = document.createElement('label')
            const label3 = document.createElement('label')
            const textLabel1 = document.createTextNode('1')
            const textLabel2 = document.createTextNode('2')
            const textLabel3 = document.createTextNode('3')
            const select1 = document.createElement('select')
            const select2= document.createElement('select')
            const select3 = document.createElement('select')
            select1.setAttribute('className', 'materialAssignment')
            select2.setAttribute('className', 'materialAssignment')
            select3.setAttribute('className', 'materialAssignment')

            for (let i in model.materials) {
                var opt1 = document.createElement("option")
                opt1.value = model.materials[i].tag
                opt1.text = model.materials[i].tag
                var opt2 = document.createElement("option")
                opt2.value = model.materials[i].tag
                opt2.text = model.materials[i].tag
                var opt3 = document.createElement("option")
                opt3.value = model.materials[i].tag
                opt3.text = model.materials[i].tag
                select1.add(opt1, select1.options[i])
                select2.add(opt2, select2.options[i])
                select3.add(opt3, select3.options[i])
            }
            divImg.appendChild(img)

            label1.appendChild(textLabel1)
            label2.appendChild(textLabel2)
            label3.appendChild(textLabel3)

            div1.appendChild(label1)
            div1.appendChild(select1)
            div2.appendChild(label2)
            div2.appendChild(select2)
            div3.appendChild(label3)
            div3.appendChild(select3)

            inputDiv.appendChild(div1)
            inputDiv.appendChild(div2)
            inputDiv.appendChild(div3)

            div.appendChild(divImg)
            div.appendChild(inputDiv)

        } else if (model.sectionType.C2) {
            const divImg = document.createElement('div')
            divImg.setAttribute('id', 'img')
            const img = document.createElement('img')
            img.setAttribute('src', '../../assets/icons/vigaC2-explodido.png')
            img.setAttribute('height', '120px')
            const inputDiv = document.createElement('div')
            inputDiv.setAttribute('id', 'inputDiv')
            const div1 = document.createElement('div')
            const div2 = document.createElement('div')
            const div3 = document.createElement('div')
            const label1 = document.createElement('label')
            const label2 = document.createElement('label')
            const label3 = document.createElement('label')
            const textLabel1 = document.createTextNode('1')
            const textLabel2 = document.createTextNode('2')
            const textLabel3 = document.createTextNode('3')
            const select1 = document.createElement('select')
            const select2= document.createElement('select')
            const select3 = document.createElement('select')
            select1.setAttribute('className', 'materialAssignment')
            select2.setAttribute('className', 'materialAssignment')
            select3.setAttribute('className', 'materialAssignment')

            for (let i in model.materials) {
                var opt1 = document.createElement("option")
                opt1.value = model.materials[i].tag
                opt1.text = model.materials[i].tag
                var opt2 = document.createElement("option")
                opt2.value = model.materials[i].tag
                opt2.text = model.materials[i].tag
                var opt3 = document.createElement("option")
                opt3.value = model.materials[i].tag
                opt3.text = model.materials[i].tag
                select1.add(opt1, select1.options[i])
                select2.add(opt2, select2.options[i])
                select3.add(opt3, select3.options[i])
            }
            divImg.appendChild(img)

            label1.appendChild(textLabel1)
            label2.appendChild(textLabel2)
            label3.appendChild(textLabel3)

            div1.appendChild(label1)
            div1.appendChild(select1)
            div2.appendChild(label2)
            div2.appendChild(select2)
            div3.appendChild(label3)
            div3.appendChild(select3)

            inputDiv.appendChild(div1)
            inputDiv.appendChild(div2)
            inputDiv.appendChild(div3)

            div.appendChild(divImg)
            div.appendChild(inputDiv)

        } else if (model.sectionType.rack) {
            const divImg = document.createElement('div')
            divImg.setAttribute('id', 'img')
            const img = document.createElement('img')
            img.setAttribute('src', '../../assets/icons/vigaRack-explodido.png')
            img.setAttribute('height', '120px')
            const inputDiv = document.createElement('div')
            inputDiv.setAttribute('id', 'inputDiv')
            const div1 = document.createElement('div')
            const div2 = document.createElement('div')
            const div3 = document.createElement('div')
            const label1 = document.createElement('label')
            const label2 = document.createElement('label')
            const label3 = document.createElement('label')
            const textLabel1 = document.createTextNode('1')
            const textLabel2 = document.createTextNode('2')
            const textLabel3 = document.createTextNode('3')
            const select1 = document.createElement('select')
            const select2= document.createElement('select')
            const select3 = document.createElement('select')
            select1.setAttribute('className', 'materialAssignment')
            select2.setAttribute('className', 'materialAssignment')
            select3.setAttribute('className', 'materialAssignment')

            for (let i in model.materials) {
                var opt1 = document.createElement("option")
                opt1.value = model.materials[i].tag
                opt1.text = model.materials[i].tag
                var opt2 = document.createElement("option")
                opt2.value = model.materials[i].tag
                opt2.text = model.materials[i].tag
                var opt3 = document.createElement("option")
                opt3.value = model.materials[i].tag
                opt3.text = model.materials[i].tag
                select1.add(opt1, select1.options[i])
                select2.add(opt2, select2.options[i])
                select3.add(opt3, select3.options[i])
            }
            divImg.appendChild(img)

            label1.appendChild(textLabel1)
            label2.appendChild(textLabel2)
            label3.appendChild(textLabel3)

            div1.appendChild(label1)
            div1.appendChild(select1)
            div2.appendChild(label2)
            div2.appendChild(select2)
            div3.appendChild(label3)
            div3.appendChild(select3)

            inputDiv.appendChild(div1)
            inputDiv.appendChild(div2)
            inputDiv.appendChild(div3)

            div.appendChild(divImg)
            div.appendChild(inputDiv)

        } else if (model.sectionType.angle) {
            const divImg = document.createElement('div')
            divImg.setAttribute('id', 'img')
            const img = document.createElement('img')
            img.setAttribute('src', '../../assets/icons/cantoneira-explodido.png')
            img.setAttribute('height', '120px')
            const inputDiv = document.createElement('div')
            inputDiv.setAttribute('id', 'inputDiv')
            const div1 = document.createElement('div')
            const div2 = document.createElement('div')
            const label1 = document.createElement('label')
            const label2 = document.createElement('label')
            const textLabel1 = document.createTextNode('1')
            const textLabel2 = document.createTextNode('2')
            const select1 = document.createElement('select')
            const select2= document.createElement('select')
            select1.setAttribute('className', 'materialAssignment')
            select2.setAttribute('className', 'materialAssignment')

            for (let i in model.materials) {
                var opt1 = document.createElement("option")
                opt1.value = model.materials[i].tag
                opt1.text = model.materials[i].tag
                var opt2 = document.createElement("option")
                opt2.value = model.materials[i].tag
                opt2.text = model.materials[i].tag
                select1.add(opt1, select1.options[i])
                select2.add(opt2, select2.options[i])
            }

            divImg.appendChild(img)

            label1.appendChild(textLabel1)
            label2.appendChild(textLabel2)

            div1.appendChild(label1)
            div1.appendChild(select1)
            div2.appendChild(label2)
            div2.appendChild(select2)

            inputDiv.appendChild(div1)
            inputDiv.appendChild(div2)

            div.appendChild(divImg)
            div.appendChild(inputDiv)

        } else if (model.sectionType.plate) {
            const divImg = document.createElement('div')
            divImg.setAttribute('id', 'img')
            const img = document.createElement('img')
            img.setAttribute('src', '../../assets/icons/plate-hover2.png')
            img.setAttribute('height', '120px')
            const inputDiv = document.createElement('div')
            inputDiv.setAttribute('id', 'inputDiv')
            const div1 = document.createElement('div')
            const select1 = document.createElement('select')
            select1.setAttribute('className', 'materialAssignment')

            for (let i in model.materials) {
                var opt1 = document.createElement("option")
                opt1.value = model.materials[i].tag
                opt1.text = model.materials[i].tag
                select1.add(opt1, select1.options[i])
            }

            divImg.appendChild(img)

            div1.appendChild(select1)

            inputDiv.appendChild(div1)

            div.appendChild(divImg)
            div.appendChild(inputDiv)

        } else {
            var paragraph = document.createElement('p')
            const text = document.createTextNode(window.i18n.__('It is not possible apply the material. Define the geometry of the profile.'))
            paragraph.appendChild(text)
            div.appendChild(paragraph)
        }
    }
}

function openMeshVisualizer() {
    const elementsize = document.getElementById('elementSize').value
    const elementMethod = document.getElementsByName('method')
    if (elementsize != '') {
        var model = readData('model.json')
        for (section in model.sectionType) {
            if (model.sectionType[section]) {
                document.getElementById('visualizeButton').style.display = 'none'
                document.getElementById('preloader').style.display = 'block'
                model.meshProperties.elementSize = parseFloat(elementsize.replace(',', '.'))
                model.meshProperties.method = parseFloat((elementMethod[0].checked? 0 : 1))

                if (Object.keys(model.loadProperties).length == 0) {
                    model.loadProperties = {
                        points:3
                    }
                }
                if (!model.sectionProperties.materialAssignment) {
                    model.sectionProperties.materialAssignment = [1,1,1]
                }
                writeData(model, 'model.json')
                runPreview()
                return
            }
            
        }
        ipcRenderer.send('create-dialog', {title: window.i18n.__('Define the geometry.'), description: ''})        
    } else {
        ipcRenderer.send('create-dialog', {title: window.i18n.__('Define the finite element size.'), description: ''})
    }
}

function runPreview() {
    const electron = require('electron')
    let app = electron.app ? electron.app : electron.remote.app
    const spawn = require('child_process').spawn
    const userDataPath = ipcRenderer.sendSync('get-user-data')
    const pathToModel = path.join(userDataPath, 'data/', 'model.json')
    // const process = spawn('python', ['../../engine/preview.py', pathToModel])
    const process = spawn('python', [app.getAppPath() + '/engine/preview.py', pathToModel])
   
    // const process = spawn(path.resolve('engine/dist/main'), props)

    process.stdout.on('data', (data) => {
        const output = data.toString()
        console.log(output)
        document.getElementById('preloader').style.display = 'none'
        document.getElementById('visualizeButton').style.display = 'block'

    })
}