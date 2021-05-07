function writeData(data, name) {
    const path = require('path')
    const fs = require('fs')

    const userDataPath = ipcRenderer.sendSync('get-user-data')
    fs.writeFileSync(path.join(userDataPath, 'data/', name), JSON.stringify(data), function(err) {
        ipcRenderer.send('create-dialog', {title: 'Erro', description: err})
    })
}

function readData(name) {
    const path = require('path')
    const fs = require('fs')

    const userDataPath = ipcRenderer.sendSync('get-user-data')
    const jsonData = fs.readFileSync(path.join(userDataPath, 'data/', name), 'utf8', function(err) {
        ipcRenderer.send('create-dialog', {title: 'Erro', description: err})
    })
    var data = JSON.parse(jsonData)
    return data
}

module.exports = {writeData, readData}