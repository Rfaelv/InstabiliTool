const texts = [
    "Axial load",
    "View axes",
    "Type",
    "Point load",
    "Distributed load",
    "Eccentricity",
    "x",
    "y",
    "The load will be evenly distributed across the cross section of the profile.",
    "Apply",
    "Cancel"
]

const labels = document.getElementsByClassName('text')

for (let i = 0; i < texts.length; i ++) {  
    labels[i].appendChild(document.createTextNode(i18n.__(texts[i])))
}