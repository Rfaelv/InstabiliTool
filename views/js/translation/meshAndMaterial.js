const texts = [
    "Mesh ann material",
    "Element size",
    "Method",
    "Free",
    "Mapped",
    "Material",
    "Apply",
    "Cancel"
]

const labels = document.getElementsByClassName('text')

for (let i = 0; i < texts.length; i ++) {  
    labels[i].appendChild(document.createTextNode(i18n.__(texts[i])))
}