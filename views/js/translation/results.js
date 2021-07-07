const texts = [
    "Results",
    "Failed to generate image. The problem is probably due to the version of openGL installed on your computer. try to update it.",
]

const labels = document.getElementsByClassName('text')

for (let i = 0; i < texts.length; i ++) {  
    labels[i].appendChild(document.createTextNode(i18n.__(texts[i])))
}