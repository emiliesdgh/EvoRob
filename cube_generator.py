import xml.etree.ElementTree as ET
from xml.dom import minidom
import numpy as np

# Créer l'élément racine <mujoco>
mujoco = ET.Element("mujoco", attrib={"model": "tensegrity"})

# Sous-élément <worldbody>
worldbody = ET.SubElement(mujoco, "worldbody")

# Créer une série de cubes espacés régulièrement
nb_cubes = 20
cube_size = 0.4
for i in range(-nb_cubes,nb_cubes,1): 
    for j in range(-nb_cubes,nb_cubes,1): 
        #generrate a number between 0.5 and 1
        size = np.random.uniform(0.01, 0.21)
        # color = np.random.uniform(0.6, 1, 3)
        # color = f"{color[0]} {color[1]} {color[2]} 1"

        if (i+j)%2 == 0:
            color = "0.8 0.95 0.77 1"
        else:
            color = "1 1 1 1"
        
        ET.SubElement(worldbody, "geom", {
            "name": f"cube_{i}_{j}",
            "type": "box",
            "size": f"{cube_size} {cube_size} {size}",
            "pos": f"{i*cube_size*2} {j*cube_size*2} {size/2}",
            "rgba": color #f"{color}"
        })

# Fonction pour indenter correctement l'XML
def prettify(elem):
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

# Écrire dans un fichier avec sauts de ligne et indentation
with open("generated_world.xml", "w") as f:
    f.write(prettify(mujoco))
