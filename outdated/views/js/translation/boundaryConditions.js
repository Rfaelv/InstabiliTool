const texts = [
    "Boundary conditions",
    "View axes",
    "Position in z axes",
    "Fix",
    "All",
    "Fix",
    "All",
    "Fix",
    "All",
    "Advanced",
    "Table",
    "Search",
    "Download example table",
    "Apply",
    "Cancel"
]

const labels = document.getElementsByClassName('text')

for (let i = 0; i < texts.length; i ++) {  
    labels[i].appendChild(document.createTextNode(i18n.__(texts[i])))
}