const { readData } = require('../../modules/writeAndReadData')
const { ipcRenderer} = require('electron')
const fs = require('fs')
const path = require('path')

// const nsteps = readData('settings.json').nonlinearAnalysis.nsteps
const nsteps = 5
const pathToLaunchAnsys = path.join(ipcRenderer.sendSync('get-user-data'), 'data/ansys')

const progress = setInterval(() => {
    var currentNumber = 0

    new Promise((resolve, reject) => {
        fs.readdir(pathToLaunchAnsys, (err, files) => {
            if (err) throw err
            
            for (const file of files) {
                var number = file.split('.')[1].slice(1)
                number = parseInt(number)
                if (typeof(number) == 'number') {
                    if (number > currentNumber) {
                        currentNumber = number
                    }
                }
            }
            resolve(currentNumber)
        })
    }).then((result) => {
        const currentProgressNumber = Math.round(result / nsteps * 100)
        move(currentProgressNumber)

        if (currentProgressNumber == 100) {
            clearInterval(progress)
        }
    })
}, 1000)
    
// async function refreshProgress() {
//     var currentNumber = 0

//     new Promise((resolve, reject) => {
//         fs.promises.readdir(pathToLaunchAnsys, (err, files) => {
//             if (err) throw err
            
//             for (const file of files) {
//             var number = file.split('.')[1].slice(1)
//             console.log(number)
//             number = parseInt(number)
//             if (typeof(number) == 'number') {
//                 console.log(number)
//                 if (number > currentNumber) {currentNumber = number}
//             }
//             }
//             // console.log(currentNumber)
//             resolve(currentNumber)
//         })
//     }).then((result) => {return result})
// }

function move(currentProgress) {
    var bar = document.getElementById('bar')
    var progressNumber = document.getElementById('progress-number')

    bar.style.width = currentProgress + '%'
    progressNumber.innerHTML = currentProgress + '%'

    if (currentProgress >= 5) {
        progressNumber.style.display = 'block'
    }
}

// var width = 1
// var id = setInterval(frame, 1000);
// function frame() {
//     if (width >= 100) {
//         clearInterval(id);
//     } else {
//         width++; 
//         move(width)
//     }
// }