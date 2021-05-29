const { ipcRenderer } = require('electron')
const {readData} = require('../../modules/writeAndReadData')
const path = require('path')

var currentResultIndex = 0

const result = readData('model.json').result

const resultlabel = document.getElementById('result')
const resultimg = document.getElementById('img')

const resultText = `${i18n.__('Critical load')} = ${result[0].value}`

resultlabel.appendChild(document.createTextNode(resultText))
// resultimg.src = result[0].imgUrl
resultimg.src = '../../assets/movie6.gif'

document.getElementById('bt-next')
    .addEventListener('click', next)

document.getElementById('bt-previus')
    .addEventListener('click', previous)

function next() {
    currentResultIndex += 1
    if (result.length == currentResultIndex) {
        currentResultIndex = 0
    }
    const resultText = `${i18n.__('Critical load')} = ${result[currentResultIndex].value}`
    resultlabel.innerText = resultText

    // resultimg.src = result[currentResultIndex].imgUrl
    resultimg.src = '../../assets/movie6.gif'
}

function previous() {
    currentResultIndex -= 1
    if (currentResultIndex < 0) {
        currentResultIndex = result.length - 1
    }
    const resultText = `${i18n.__('Critical load')} = ${result[currentResultIndex].value}`
    resultlabel.innerText = resultText
    resultimg.src = result[currentResultIndex].imgUrl
    resultimg.src = '../../assets/movie6.gif'
}
 