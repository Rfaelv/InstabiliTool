const texts = [
    "General analysis options",
    "Shell 181 Element",
    "Element stiffness",
    "Bending and membrane stiffness (default)",
    "Membrane stiffness only",
    "Stress/strain evaluation only",
    "Integration option",
    "Full integration with incompatible modes",
    "Reduced integration with hourglass control (default)",
    "Curved shell formulation",
    "Standard shell formulation (default)",
    "Advanced curved-shell formation",
    "Simplified curved-shell formation",
    "Apply",
    "Cancel"
]

const labels = document.getElementsByClassName('text')

for (let i = 0; i < texts.length; i ++) {  
    labels[i].appendChild(document.createTextNode(i18n.__(texts[i])))
}