const { ipcRenderer, dialog } = require('electron')
const {readData, writeData} = require('../../modules/writeAndReadData')
const fs = require('fs')
const path = require('path')

configMaterialInput()

const applybutton = document.getElementById('apply')
applybutton.addEventListener('click', setMeshAndMaterialAssignment)

const cancelbutton = document.getElementById('cancel')
cancelbutton.addEventListener('click', cancel)

document.getElementById('elementSize').focus()


function setMeshAndMaterialAssignment() {
    const elementSize = document.getElementById('elementSize')
    const elementMethod = document.getElementsByName('method')
    const selects = document.getElementsByClassName('materialAssignment')

    if (elementSize.value == '' || (!elementMethod[0].checked && !elementMethod[1].checked)) {
        ipcRenderer.send('create-dialog', {title: 'Erro', description: 'Preencha todos os campos.'})
        if (elementSize.value == '') {
            elementSize.focus()
        }
        return
    }

    var model = readData('model.json')
    model.meshProperties = {
        elementSize: parseFloat(elementSize.value.replace(',', '.')),
        method: parseFloat((elementMethod[0].checked? 0 : 1)),
    }
    var materialAssignmentList = []
    for (select of selects) {
        materialAssignmentList.push(select.options[select.selectedIndex].value)
    }
    model.sectionProperties.materialAssignment = materialAssignmentList
    writeData(model, 'model.json')
    // ipcRenderer.send('delete-current-window')
}


function cancel() {
    ipcRenderer.send('delete-current-window')
}

function configMaterialInput() {
    var div = document.getElementById('addMateial')
    const model = readData('model.json')

    if(model.materials.length == 0) {
        var paragraph = document.createElement('p')
        const text = document.createTextNode('Crie pelo menos um material para adicionar ao perfil.')
        paragraph.appendChild(text)
        div.appendChild(paragraph)
    } else if(model.materials.length == 1) {
        var paragraph = document.createElement('p')
        const text = document.createTextNode(`${model.materials[0].tag} será utilizado para todo o perfil. Para utilizar mais de um material no perfil, crie outros e retorne aqui.`)
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

        } else {
            var paragraph = document.createElement('p')
            const text = document.createTextNode(`Não é possível aplicar o material. Defina a geometria do perfil.`)
            paragraph.appendChild(text)
            div.appendChild(paragraph)
        }
    }
}