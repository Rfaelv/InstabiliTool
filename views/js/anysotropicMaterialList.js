const { ipcRenderer } = require('electron')

document.getElementById('add')
    .addEventListener('click', add)
document.getElementById('edit')
    .addEventListener('click', edit)
document.getElementById('delete')
    .addEventListener('click', del)
document.getElementById('cancel')
    .addEventListener('click', cancel)
document.getElementById('ok')
    .addEventListener('click', finalize)
window.addEventListener('load', refreshData)
window.addEventListener('focus', refreshData)

function add() {
    ipcRenderer.send('create-window', {
        width:820,
        height:350,
        path:'views/html/materialPropertiesAny.html'
    })
}

function edit() {
    alert(document.querySelector('input[name="materialList"]:checked').value)
    localStorage.setItem('selected-material', document.querySelector('input[name="materialList"]:checked').value)
    ipcRenderer.send('create-window', {
        width:820,
        height:350,
        path:'views/html/materialPropertiesAny.html'
    })
}

function del() {
    alert('del')
}

function cancel() {
    ipcRenderer.send('delete-current-window')
}

function finalize() {
    alert('finalize')
}
function refreshData() {
    generateList()
}

function generateList() {
    const materialData = null

    for (var key in materialData) {
        if (materialData[key].materialType[localStorage.getItem('current-material-type')]) {
            var div = document.createElement('div')
            div.setAttribute('id', 'list-item') 

            var radio = document.createElement('input')
            radio.setAttribute('id', key)
            radio.setAttribute('name', 'isotropicMaterialList')
            radio.setAttribute('value', key)

            var label = createElement('label')
            label.setAttribute('id', 'label-list')
            label.setAttribute('for', key)

            var materialTag = document.createTextNode(key)

            label.appendChild(materialTag)
            
            div.appendChild(radio)
            div.appendChild(label)

            document.getElementById('list').appendChild(div)
        }
    }
}