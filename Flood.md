> - The **flood** and **flood2** shaders adds a number of layers of voxels, of your selected color, upwards from the bottom of your volume. Voxels are only added to empty space and won't replace existing voxels.
> - **flood2** is similar to **flood**, except flooding stops when a voxel is encountered so that exclosed spaces aren't filled.

<!-- TOC -->
- [Arguments](#arguments)
- [Shaders](#shaders)
- [Examples](#examples)

## Arguments

Argument | Description
--------- | -----------
**Height** | Height of the flood

## Shaders

<!-- SAMPLE flood_shaders 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/flood_1.png" alt="Example of the flood shader"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/flood_2.png" alt="Example of the flood2 shader"></td>
	</tr>
	<tr>
		<th><code>flood</code></th>
		<th><code>flood2</code></th>
	</tr>
</table>
<!-- END -->

## Examples

<!-- SAMPLE flood_examples 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/flood_example0.jpg" alt=""></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/flood_example1.jpg" alt=""></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/flood_example2.jpg" alt=""></td>
	</tr>
	<tr>
		<td valign="top">Original</td>
		<td valign="top">Using <code>flood</code> to submerge models in water using a glass material</td>
		<td valign="top">Using <code>flood</code> to engulf in fog using cloud materials</td>
	</tr>
</table>
<!-- END -->
