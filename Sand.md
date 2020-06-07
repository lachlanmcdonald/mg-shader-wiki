> The **sand** and **sand2** shaders add a layer voxels on top of voxels matching the selected colour. Voxels are added randomly and only added when the voxel beneath has adjacent voxels, creating the effect of a rough pile of sand. The number of adjacent neighbours affects the randomness, with a higher number of neighbours increasing the odds a voxel will be added.

## Parameters

Voxels are added on top of voxels matching the selected color.

- **Color**: Color index for the voxels. If set to `0`, the selected color index is used instead.
