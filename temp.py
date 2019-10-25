import numpy as np
import os, glob

import get_perimeter_nodes as gpn
import visualize_network

txt_files=glob.glob(os.path.join("datasets", "*.txt"))

for txt_file in txt_files:

	data=np.loadtxt(txt_file)
	hull=gpn.get_hull(data)
	visualize_network.display_points(data, hull, txt_file.replace(".txt", ".png"))
