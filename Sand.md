> - The **sand** and **sand2** shaders add a layer of voxels on top of voxels matching the selected color.
> - **sand** will only add voxels when the adjacent voxels match the selected color. Whereas, **sand2** will add voxels if there are adjacent voxels of any color.

Voxels are added randomly and only added when the voxel beneath has adjacent voxels, creating the effect of a rough pile of sand. The number of adjacent neighbors affects the randomness, with a higher number of neighbors increasing the odds a voxel will be added.

- [Parameters](#parameters)
- [Examples](#examples)

## Parameters

Voxels are added on top of voxels matching the selected color.

Parameter | Description
--------- | -----------
**Color** | Color index of added voxels. If set to `0`, the selected color index is used instead

## Examples

<table>
    <tr>
        <td width="33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/sand1.png" alt=""></td>
        <td width="33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/sand2.png" alt=""></td>
        <td width="33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/sand3.png" alt=""></td>
    </tr>
</table>
