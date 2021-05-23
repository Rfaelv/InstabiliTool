const labels = document.getElementsByClassName('text')

for (let i = 0; i < labels.length; i ++) {  
    labels[i].appendChild(document.createTextNode(i18n.__(labels[i].value)))
}