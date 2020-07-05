> - The **flood** and **flood2** shaders adds a number of layers of voxels, of your selected color, upwards from the bottom of your volume. Voxels are only added to empty space and won't replace existing voxels.
> - **flood2** is similar to **flood**, except flooding stops when a voxel is encountered so that exclosed spaces aren't filled.

<!-- TOC -->
- [Parameters](#parameters)
- [Examples](#examples)

## Parameters

Parameter | Description
--------- | -----------
**Height** | Height of the flood

## Examples

<table>
    <tr>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/flood_1.png" alt=""></td>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/flood_2.png" alt=""></td>
    </tr>
	<tr>
		<th><code>flood</code></th>
		<th><code>flood2</code></th>
	</tr>
</table>
