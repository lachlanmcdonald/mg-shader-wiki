> **outline** and **outline2** shaders replaces all voxels which match your selected color, that are adjacent to another voxel of a different color, with your chosen color.
> **outline2** produces thinner lines.

<!-- TOC -->
- [Arguments](#arguments)
- [Examples](#examples)

## Arguments

Argument | Description
--------- | -----------
**Color** | Color index to replace voxels (setting the index to `0` will remove voxels)

## Examples

<!-- SAMPLE outline_examples 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/outline1.png" alt=""></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/outline2.png" alt=""></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/outline3.png" alt=""></td>
	</tr>
	<tr>
		<td valign="top">Original</td>
		<td valign="top"><code>outline</code></td>
		<td valign="top"><code>outline2</code></td>
	</tr>
</table>
<!-- END -->
