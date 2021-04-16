var geometryIcons = document.getElementsByClassName('geometryIcon')

Array.prototype.forEach.call(geometryIcons, setEventListener)
function setEventListener(item) {
    item.addEventListener('mouseenter', e => {
        const newPath = item.src.slice(0, -4) + '-hover2.png'
        item.src = newPath
    })
    item.addEventListener('mouseout', () => {
        const newPath = item.src.slice(0, -11) + '.png'
        item.src = newPath
    })
}
