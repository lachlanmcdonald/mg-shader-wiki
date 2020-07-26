> - The **sand** and **sand2** shaders add a layer of voxels on top of voxels matching the selected color.
> - **sand** will only add voxels when the adjacent voxels match the selected color. Whereas, **sand2** will add voxels if there are adjacent voxels of any color.

Voxels are added randomly and only added when the voxel beneath has adjacent voxels, creating the effect of a rough pile of sand. The number of adjacent neighbors affects the randomness, with a higher number of neighbors increasing the odds a voxel will be added.

<!-- TOC -->
- [Arguments](#arguments)
- [Examples](#examples)

## Arguments

Voxels are added on top of voxels matching the selected color.

Argument | Description
--------- | -----------
**Color** | Color index of added voxels. If set to `0`, the selected color index is used instead

## Examples

<!-- SAMPLE sand_examples 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/sand_example00.png" alt=""></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/sand_example01.png" alt=""></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/sand_example02.png" alt=""></td>
	</tr>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/sand_example10.png" alt=""></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/sand_example11.png" alt=""></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/sand_example12.png" alt=""></td>
	</tr>
</table>
<!-- END -->
