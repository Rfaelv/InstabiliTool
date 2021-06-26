const texts = [
    "Units",
    "Dimensions: m",
    "Elastic moduli: N/m² - Pa",
    "Density: kg/m³"
]

const labels = document.getElementsByClassName('text')

for (let i = 0; i < texts.length; i ++) {  
    labels[i].appendChild(document.createTextNode(i18n.__(texts[i])))
}