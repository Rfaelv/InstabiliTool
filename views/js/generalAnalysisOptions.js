const { ipcRenderer} = require('electron')
const fs = require('fs')
const path = require('path')
const { writeData, readData } = require('../../modules/writeAndReadData')

orderOptions()

const applybutton = document.getElementById('apply')
applybutton.addEventListener('click', setGeneralAnalysisOptions)

const cancelbutton = document.getElementById('cancel')
cancelbutton.addEventListener('click', cancel)

function setGeneralAnalysisOptions() {
    const elementStiffness = document.getElementById('element-stiffness')
    const integrationOption = document.getElementById('integration-option')
    const curvedShellFormulation = document.getElementById('curved-shell-formulation')

    var settings = readData('settings.json')

    settings.general.elementStiffness = parseInt(
        elementStiffness.options[elementStiffness.selectedIndex].value)
    settings.general.integrationOption = parseInt(
        integrationOption.options[integrationOption.selectedIndex].value)
    settings.general.curvedShellFormulation = parseInt(
        curvedShellFormulation.options[curvedShellFormulation.selectedIndex].value)
    
    writeData(settings, 'settings.json')

    ipcRenderer.send('delete-current-window')
}

function orderOptions() {
    const settings = readData('settings.json')

    var elementStiffness = document.getElementById('element-stiffness')
    var integrationOption = document.getElementById('integration-option')
    var curvedShellFormulation = document.getElementById('curved-shell-formulation')

    elementStiffness.selectedIndex = settings.general.elementStiffness
    integrationOption.selectedIndex = settings.general.integrationOption == 0 ? 1 : 0
    curvedShellFormulation.selectedIndex = settings.general.curvedShellFormulation
}

function cancel() {
    ipcRenderer.send('delete-current-window')
}