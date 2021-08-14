const { ipcRenderer } = require('electron')
const path = require('path')


const userDataPath = ipcRenderer.sendSync('get-user-data')
const pathToMeshImage = path.join(userDataPath, '/data/images/mesh.png')

document.getElementById('meshImg').src = pathToMeshImage