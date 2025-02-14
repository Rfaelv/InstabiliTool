const texts = [
    "Material axes",
    "The material axes are defined on the plates as is shown below.",
]

const labels = document.getElementsByClassName('text')

for (let i = 0; i < texts.length; i ++) {  
    labels[i].appendChild(document.createTextNode(i18n.__(texts[i])))
}