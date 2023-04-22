# Edge Selection by Angle in Maya

This Python script is a utility for Autodesk Maya that allows users to select edges between two faces if the angle between those faces is below a given threshold.

## Function

The script contains one primary function, `selectEdgesByAngle(angle)`, which takes a single argument: the angle threshold in degrees. It selects edges between two faces in Maya if the angle between those faces is below the given threshold.

## How to use

1. Save the script as `selectEdgesByAngle.py` in your Maya scripts folder. The default location for the scripts folder is:
   - Windows: `C:\Users\<username>\Documents\maya\<version>\scripts`
   - macOS: `~/Library/Preferences/Autodesk/maya/<version>/scripts`
   - Linux: `~/maya/<version>/scripts`
   
   Replace `<username>`, `<version>` with your username and your Maya version, respectively.
   
2. Open Autodesk Maya, and open the Script Editor by navigating to `Windows > General Editors > Script Editor`.
3. In the Script Editor, switch to the Python tab.
4. Import the script and call the `selectEdgesByAngle(angle)` function with the desired angle threshold in degrees:

   ```python
   import selectEdgesByAngle

   selectEdgesByAngle.main(30)
   ```

5. Execute the script by selecting the lines you just entered and pressing the `Execute` button or the `Enter/Return` key on your keyboard while holding the `Ctrl` key (Windows/Linux) or `Cmd` key (macOS).

## How it works

The script calculates the angle between two connected faces using the following math:

1. Convert the angle threshold from degrees to radians: `radians = math.radians(angle)`
2. Compute the dot product of the two face normals, `v1` and `v2`: `deg = v1.angle(v2)`
3. Check if the computed angle `deg` is greater than or equal to the given threshold in radians: `if deg >= radians:`

The angle between two vectors `v1` and `v2` can be calculated as:

$$c=\alpha_f(c_f \cdot c_f) + (1 - \alpha_f) c_b$$

Here, $\theta$ is the angle between the two vectors $\mathbf{v_1}$ and $\mathbf{v_2}$, $\mathbf{v_1} \cdot \mathbf{v_2}$ is the dot product of the vectors, and $||\mathbf{v_1}||$ and $||\mathbf{v_2}||$ are the magnitudes of the vectors.

The script uses Maya's API to interact with the scene, selecting the edges that meet the angle criteria.

### Additional notes

- The script avoids selecting edges with non-manifold topology or border edges by checking the length of the connected faces: `if len(faces) != 2:`
- The resulting edge selection is stored in a new selection list, which is then set as the active selection in Maya: `om.MGlobal.setActiveSelectionList(newSelList)`
