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
    if (i == 3) {
        labels[i].title = i18n.__('A free mesh has no restrictions in terms of element shapes,\nand has no specified pattern applied to it.')
    }
    if (i == 4) {
        labels[i].title = i18n.__('A mapped mesh is restricted in terms of the element\nshape it contains and the pattern of the mesh.')
    }
}