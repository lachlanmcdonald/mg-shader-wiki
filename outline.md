> **outline** and **outline2** shaders replaces all voxels which match your selected color, that are adjacent to another voxel of a different color, with your chosen color.
> **outline2** produces thinner lines.

- [Parameters](#parameters)
- [Examples](#examples)

## Parameters

- **Color**: Color index to replace voxels (setting the index to `0` will remove voxels)

## Examples

<table>
    <tr>
        <td width="33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/outline1.png" alt="">Original<td>
        <td width="33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/outline2.png" alt=""><code>outline</code></td>
        <td width="33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/outline3.png" alt=""><code>outline2</code></td>
    </tr>
</table>