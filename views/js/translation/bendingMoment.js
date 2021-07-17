const texts = [
    "Bending moment",
    "Bending type",
    "Four point bending",
    "Three point bending",
    "Direct bending",
    "Lshear",
    "Direction",
    "x",
    "y",
    "Apply",
    "Cancel"
]

const labels = document.getElementsByClassName('text')

for (let i = 0; i < texts.length; i ++) {  
    labels[i].appendChild(document.createTextNode(i18n.__(texts[i])))
}