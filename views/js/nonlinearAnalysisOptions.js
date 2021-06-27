const { ipcRenderer} = require('electron')
const { writeData, readData } = require('../../modules/writeAndReadData')

const settings = readData('settings.json')
const loadFactor = document.getElementById('load-factor')
const initialDeformationFactor = document.getElementById('inicial-deformation-factor')
loadFactor.value = settings.nonlinearAnalysis.loadFactor
initialDeformationFactor.value = settings.nonlinearAnalysis.initialDeformationFactor
loadFactor.focus()

document.getElementById('load').title = window.i18n.__('The critical load of linear analysis is updated with this factor to be applied in nonlinear analysis.')
document.getElementById('deformation').title = window.i18n.__('This factor will be applied to the minor tickness of the profile and the result will be applied to the buckling deformation resulting in linear analysis.')

const applybutton = document.getElementById('apply')
applybutton.addEventListener('click', setNonlinearAnalysisOptions)

const cancelbutton = document.getElementById('cancel')
cancelbutton.addEventListener('click', cancel)

function setNonlinearAnalysisOptions() {
    var settings = readData('settings.json')
    settings.nonlinearAnalysis.loadFactor = parseFloat(loadFactor.value.replace(',', '.'))
    settings.nonlinearAnalysis.initialDeformationFactor = parseFloat(
        initialDeformationFactor.value.replace(',', '.')
    )

    writeData(settings, 'settings.json')

    ipcRenderer.send('delete-current-window')
}

function cancel() {
    ipcRenderer.send('delete-current-window')
}