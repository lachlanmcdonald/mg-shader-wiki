> The **Grass [brush](Brush-Shaders)** generates random columns of voxels with a constant distribution; similar to grass or small plants.
>
>  The height of the grass is affected by the brush height and the color of the voxels is determined by the selected colors in the palette.
>
> This shader is similar to the [Grass Fit shader](Grass-Fit), which it is applied to the entire volume.

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
**Direction** | When `0`, line extends upwards. When `1`, line hangs downwards
**Mode** | Color mode (see below)
**Density** | Size of the area in which a line should be generated. Increasing density will increase the spacing between lines
**Growth** | Affects the growth of the lines. `50` is a evenly-distributed growth. Higher or lower values will overgrow or stymied the growth, respectively
**Seed** | Global seed

### Mode

There are 4 distinct color modes for generating voxels, as outlined below:

<!-- SAMPLE grass modes 2 -->
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

### Density

<!-- SAMPLE grass density 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/grass_density1.png" alt="Example of a 'Density' value of 1"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/grass_density2.png" alt="Example of a 'Density' value of 2"></td>
	</tr>
	<tr>
		<th>Density: <code>1</code></th>
		<th>Density: <code>2</code></th>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/grass_density3.png" alt="Example of a 'Density' value of 3"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/grass_density4.png" alt="Example of a 'Density' value of 4"></td>
	</tr>
	<tr>
		<th>Density: <code>3</code></th>
		<th>Density: <code>4</code></th>
	</tr>
</table>
<!-- END -->

### Growth

<!-- SAMPLE grass growth 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/grass_growth000.png" alt="Example of a 'Growth' value of 0"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/grass_growth050.png" alt="Example of a 'Growth' value of 50"></td>
	</tr>
	<tr>
		<th>Growth: <code>0</code></th>
		<th>Growth: <code>50</code></th>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/grass_growth075.png" alt="Example of a 'Growth' value of 75"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/grass_growth100.png" alt="Example of a 'Growth' value of 100"></td>
	</tr>
	<tr>
		<th>Growth: <code>75</code></th>
		<th>Growth: <code>100</code></th>
	</tr>
</table>
<!-- END -->

## Examples

<!-- SAMPLE grass examples 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/grass_example0.png" alt="Example"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/grass_example1.png" alt="Example"></td>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/grass_example2.png" alt="Example"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/grass_example3.png" alt="Example"></td>
	</tr>
</table>
<!-- END -->

## Notes

- The `grass_inv` shader was replaced by the **Direction** parameter
