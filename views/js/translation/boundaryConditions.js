const texts = [
    "Boundary conditions",
    "See axes",
    "Extremities",
    "Fix",
    "All",
    "Fix",
    "All",
    "Fix",
    "All",
    "Span",
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