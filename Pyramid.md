> The **pyramid** and **pyramid2** shaders add a layer of voxel on top of voxels matching the selected color. A voxel is only added when the voxel beneath has adjacent voxels, creating the effect of a pyramid.

**pyramid** will only add voxels when the adjacent voxels match the selected color. Whereas, **pyramid2** will add voxels if there are adjacent voxels of any color.

## Parameters

Voxels are added on top of voxels matching the selected color.

- **Color** Color index for the voxels. If set to `0`, the selected color index is used instead. 

## Axis Modes

When no axis modes are set, the shader will form a square pyramid. However, if either X or Y axis modes are set, the shader will form a pyramid with the slope facing the X or Y axis, respectively. Setting the Z-axis mode has no effect.
