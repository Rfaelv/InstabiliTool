const texts = [
    "Nonlinear analysis options",
    "Load factor",
    "Initial deformation factor",
    "Apply",
    "Cancel"
]

const labels = document.getElementsByClassName('text')

for (let i = 0; i < texts.length; i ++) {  
    labels[i].appendChild(document.createTextNode(i18n.__(texts[i])))
}