const { ipcRenderer} = require('electron')
const { writeData, readData } = require('../../modules/writeAndReadData')

const settings = readData('settings.json')
const nmodes = document.getElementById('nmodes')
nmodes.value = settings.linearAnalysis.nmodes
nmodes.focus()

const applybutton = document.getElementById('apply')
applybutton.addEventListener('click', setLinearAnalysisOptions)

const cancelbutton = document.getElementById('cancel')
cancelbutton.addEventListener('click', cancel)

function setLinearAnalysisOptions() {
    // const nmodes = document.getElementById('nmodes')

    var settings = readData('settings.json')
    settings.linearAnalysis.nmodes = parseInt(nmodes.value)

    writeData(settings, 'settings.json')

    ipcRenderer.send('delete-current-window')
}

function cancel() {
    ipcRenderer.send('delete-current-window')
}