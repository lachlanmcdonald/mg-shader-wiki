> - The **pyramid** and **pyramid2** shaders add a layer of voxel on top of voxels matching the selected color. A voxel is only added when the voxel beneath has adjacent voxels, creating the effect of a pyramid.
> - **pyramid** will only add voxels when the adjacent voxels match the selected color. Whereas, **pyramid2** will add voxels if there are adjacent voxels of any color.

- [Parameters](#parameters)
- [Axis Modes](#axis-modes)

## Parameters

Voxels are added on top of voxels matching the selected color.

- **Color**: Color index (if set to `0`, the selected color index is used instead)

## Axis Modes

When no axis modes are set, the shader will form a square pyramid. However, if either X or Y axis modes are set, the shader will form a pyramid with the slope facing the X or Y axis, respectively. Setting the Z-axis mode has no effect.

<img width="25%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/py7.png" alt="">

## Examples

<table>
    <tr>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/py1.png" alt=""></td>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/py2.png" alt=""></td>
    </tr>
    <tr>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/py3.png" alt=""></td>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/py4.png" alt=""></td>
    </tr>
    <tr>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/py5.png" alt=""></td>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/py6.png" alt=""></td>
    </tr>
</table>