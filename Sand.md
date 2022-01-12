> The **`sand`** and **`sand2`** shaders add a layer of voxels on top of voxels matching the selected colors.
>
> `sand` will only add voxels when the adjacent voxels are one of the selected colors. Whereas, `sand2` will add voxels if there are adjacent voxels of any color.

<!-- TOC -->
- [Parameters](#parameters)
- [Mode](#mode)
- [Examples](#examples)

## Parameters

Voxels are added on top of voxels matching the selected color. Voxels are added randomly and only added when the voxel beneath has adjacent voxels, creating the effect of a rough pile of sand. The number of adjacent neighbors affects the randomness, with a higher number of neighbors increasing the odds a voxel will be added.

Parameter | Description
--------- | -----------
**Mode** | Color mode (see below)
**Threshold** | Skews how often sand is added. Values closer to `0` quickly create peaks, where as values closer to `100` will add many more voxels.

## Mode

There are 3 distinct color modes for generating voxels, as outlined below:

<!-- SAMPLE sand modes 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/sand_mode0.png" alt="Example of a 'Mode' value of 0"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/sand_mode1.png" alt="Example of a 'Mode' value of 1"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/sand_mode2.png" alt="Example of a 'Mode' value of 2"></td>
	</tr>
	<tr>
		<th>Mode: <code>0</code></th>
		<th>Mode: <code>1</code></th>
		<th>Mode: <code>2</code></th>
	</tr>
	<tr>
		<td valign="top">The color is chosen at random from the selected colors.</td>
		<td valign="top">The color of each voxel depends on how many adjacent neighbours it has.</td>
		<td valign="top">Reverse of Mode 1.</td>
	</tr>
</table>
<!-- END -->

## Examples

<!-- SAMPLE sand examples 3 -->
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
