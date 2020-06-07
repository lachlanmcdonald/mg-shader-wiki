> The `py` and `py2` shaders add a layer of voxel on top of voxels matching the selected colour. A voxel is only added when the voxel beneath has adjacent voxels, creating the effect of a pyramid.

- `py` will only add voxels when the adjacent voxels match the selected color. Whereas, `py2` will add voxels if there are adjacent voxels of any color.

## Parameters

- If provided, `index` will be the color index of the added voxels. This parameter is optional; if set to `0`, the selected color index is used instead.

Each time the shader is executed, a single layer is added. To add multiple layers at once, use `-n` to set a number of iterations:

```
xs -n 50 py
xs -n 50 py2
```

## Axis Modes

When no axis modes are set, the shader will form a square pyramid. However, if either X or Y axis modes are set, the shader will form a pyramid with the slope facing the X or Y axis, respectively.
