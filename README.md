# perimeter_detection in WSN

I intend to reproduce the results from the paper [On Boundary Detection of 2-D and 3-D Wireless
Sensor Networks](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=6134480) in this repository.

- `datasets/` folder contains the `.txt` and their corresponding visualizations using matplotlib library in `.png` format.

- `calculate_virtual_coordinates.py` : 
Input: physical coordinates (it has helper functions to generate random physical coordinates also)<br>
Intermediate Step: Designate 10 random anchor nodes<br>
Output: Virtual Coordinates for every node.<br>

- `get_perimeter_nodes.py`: <br>
Input: Topology or physical coordinates<br>
Output: Convex Hull of the set of points<br>

- `tpm_from_vcs.py`:<br>
Input: Virtual Coordinates<br>
Output: Topological Coordinates<br>
Implemented as described in Dhanapala et al, 2013, IEEE/ACM TON, Topology Preserving Maps<br>

- `visualize_network.py`:<br>
Input: Set of points and their convex hull<br>
Output: Matplotlib object depicting the input.<br>
