> The **`soil`**, **`soil_replace`** shaders adds a layer of voxels of a color on top of voxels matching the selected colors. `soil` adds the voxels on top, and `soil_replace` replaces the voxels.
> 
> This shader is similar to the [`cover`](Cover) shader, except `cover` adds a layer to all voxels, where these shaders only works on the selected colours.

## Arguments

Argument | Description
--------- | -----------
**Color** | Color index
**Headroom** | The number of voxels of space that must be available above the surface voxel. Setting to a higher value will stop voxels from forming in gaps
