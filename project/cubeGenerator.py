import numpy as np


for i in range(25):

    name = f"cube{i}"
    type = "box"
    size = f"0.5 0.5 {np.random.uniform(0, 0.5)}"
    pos = f"{0+i} {0-i} 0"
    rgba = "0.8 0.95 0.77 1"
    euler = "0 0 0"
    condim = "4"

    print(f"<geom name=\"{name}\" type=\"{type}\" size=\"{size}\" pos=\"{pos}\" rgba=\"{rgba}\" euler=\"{euler}\" condim=\"{condim}\" />")

    # <geom name="cube1" type="box" size="0.5 0.5 0.5" pos="0.0 0 0" rgba="0.8 0.95 0.77 1" euler="0 0 0" condim="4" />
