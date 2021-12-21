> The **Grass Fit** shader generates random lines of voxels with a constant distribution; similar to grass or small plants. The color of the voxels is determined by the selected colors in the palette.
>
> This shader is similar to the [Grass brush shader](Grass-Brush), except this shader is applied to the entire volume.

<!-- TOC -->
- [Parameters](#parameters)
- [Mode](#mode)
- [Density](#density)
- [Growth](#growth)
- [Examples](#examples)
- [Notes](#notes)

## Parameters

Parameter | Description
--------- | -----------
**Mode** | Color mode (see below)
**Density** | Size of the area in which a line should be generated. Increasing density will increase the spacing between lines
**Height** | Size of the area in which a line should be generated. Increasing density will increase the spacing between lines
**Seed** | Global seed

## Mode

There are 4 distinct color modes for generating voxels, as outlined below:

<!-- SAMPLE grass_modes 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/grass_mode0.png" alt="Example of a 'Mode' value of 0"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/grass_mode1.png" alt="Example of a 'Mode' value of 1"></td>
	</tr>
	<tr>
		<th>Mode: <code>0</code></th>
		<th>Mode: <code>1</code></th>
	</tr>
	<tr>
		<td valign="top">The color of the line is dependant on its height.</td>
		<td valign="top">The color of each voxel in the line is chosen at random.</td>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/grass_mode2.png" alt="Example of a 'Mode' value of 2"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/grass_mode3.png" alt="Example of a 'Mode' value of 3"></td>
	</tr>
	<tr>
		<th>Mode: <code>2</code></th>
		<th>Mode: <code>3</code></th>
	</tr>
	<tr>
		<td valign="top">The color of the line is chosen at random.</td>
		<td valign="top">The color of the line is a gradient between <strong>Color A</strong> and<strong> Color B</strong> (regardless of height.)</td>
	</tr>
</table>
<!-- END -->

## Density


## Height

## Notes

- The shader will cause issues when used with the _Marquee Select_ tool (as the shader can't see voxels that are unselected.)
