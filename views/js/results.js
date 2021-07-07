const { ipcRenderer } = require('electron')
const {readData} = require('../../modules/writeAndReadData')
const path = require('path')

var currentResultIndex = 0

const result = readData('model.json').result
console.log(result)
const resultValues = result.values
const resultImg = result.img

const resultlabel = document.getElementById('result')
const resultimg = document.getElementById('img')

const resultText = `${i18n.__('Critical load')} = ${resultValues[0].value}`

resultlabel.appendChild(document.createTextNode(resultText))

if (resultImg[0]) {
    resultimg.src = resultImg[0]
} else {
    resultimg.style.display = 'none'
    document.querySelector('#info').style.display = 'block'
}
// resultimg.src = '../../assets/movie6.gif'
// var reader  = new FileReader();

// reader.addEventListener("load", function () {
//     var base64gif = reader.result // your gif in base64 here
//     resultimg.src= base64gif
// }, false)


// reader.readAsDataURL('../../assets/movie6.gif');

// function toDataURL(url, callback) {
//     var xhr = new XMLHttpRequest();
//     xhr.onload = function() {
//       var reader = new FileReader();
//       reader.onloadend = function() {
//         callback(reader.result);
//       }
//       reader.readAsDataURL(xhr.response);
//     };
//     xhr.open('GET', url);
//     xhr.responseType = 'blob';
//     xhr.send();
// }
  
// toDataURL('../../assets/movie6.gif', function(dataUrl) {
//     console.log('RESULT:', dataUrl)
//     resultimg.src = dataUrl
// })


document.getElementById('bt-next')
    .addEventListener('click', next)

document.getElementById('bt-previus')
    .addEventListener('click', previous)

function next() {
    currentResultIndex += 1
    if (resultValues.length == currentResultIndex) {
        currentResultIndex = 0
    }
    const resultText = `${i18n.__('Critical load')} = ${resultValues[currentResultIndex].value}`
    resultlabel.innerText = resultText

    if (resultImg[currentResultIndex]) {
        resultimg.src = resultImg[currentResultIndex]
        resultimg.style.display = 'flex'
        document.querySelector('#info').style.display = 'none'
    } else {
        resultimg.style.display = 'none'
        document.querySelector('#info').style.display = 'block'
    }
    // resultimg.src = '../../assets/movie6.gif'
}

function previous() {
    currentResultIndex -= 1
    if (currentResultIndex < 0) {
        currentResultIndex = resultValues.length - 1
    }
    const resultText = `${i18n.__('Critical load')} = ${resultValues[currentResultIndex].value}`
    resultlabel.innerText = resultText

    if (resultImg[currentResultIndex]) {
        resultimg.src = resultImg[currentResultIndex]
        resultimg.style.display = 'flex'
        document.querySelector('#info').style.display = 'none'
    } else {
        resultimg.style.display = 'none'
        document.querySelector('#info').style.display = 'block'
    }
    // resultimg.src = '../../assets/movie6.gif'
}
 