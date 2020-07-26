> The **Grass [brushes](Brush-Shaders)** generates randomly protruding lines of voxels with a constant distribution; similar to grass, small plants or similar surfaces. The height of the grass is affected by the brushes height.
> 
> There are two shaders, **`grass`** and **`grass_inv`**, that are functionally identical except grass protrude upwards and `grass_inv` extrudes downwards.

<!-- TOC -->
- [Arguments](#arguments)
- [Mode](#mode)
- [Density](#density)
- [Growth](#growth)
- [Examples](#examples)

## Arguments

Argument | Description
--------- | -----------
**Mode** | Color mode (see below)
**Density** | Size of the area in which a line should be generated. Increasing density will increase the spacing between lines
**Growth** | Affects the growth of the lines. `0.5` is a fairly evenly-distributed growth. Higher or lower values will overgrow or stymied the heights, respectively
**Seed** | Global seed
**Color A** | First color index
**Color B** | Last color index

Setting either of the colors to `0` will also result in empty voxels.

## Mode

There are 4 distinct color modes for generating voxels, as outlined below:

<!-- SAMPLE grass_modes 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/grass_mode0.png" alt="Example of mode of 0"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/grass_mode1.png" alt="Example of mode of 1"></td>
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
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/grass_mode2.png" alt="Example of mode of 2"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/grass_mode3.png" alt="Example of mode of 3"></td>
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

<!-- SAMPLE grass_density 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/grass_density1.png" alt="Example of a density of 1"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/grass_density2.png" alt="Example of a density of 2"></td>
	</tr>
	<tr>
		<th>Density: <code>1</code></th>
		<th>Density: <code>2</code></th>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/grass_density3.png" alt="Example of a density of 3"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/grass_density4.png" alt="Example of a density of 4"></td>
	</tr>
	<tr>
		<th>Density: <code>3</code></th>
		<th>Density: <code>4</code></th>
	</tr>
</table>
<!-- END -->

## Growth

<!-- SAMPLE grass_growth 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/grass_growth000.png" alt="Example of a growth of 0.0"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/grass_growth050.png" alt="Example of a growth of 0.5"></td>
	</tr>
	<tr>
		<th>Growth: <code>0.0</code></th>
		<th>Growth: <code>0.5</code></th>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/grass_growth075.png" alt="Example of a growth of 0.75"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/grass_growth100.png" alt="Example of a growth of 1.0"></td>
	</tr>
	<tr>
		<th>Growth: <code>0.75</code></th>
		<th>Growth: <code>1.0</code></th>
	</tr>
</table>
<!-- END -->

## Examples

<!-- SAMPLE grass_examples 2 -->
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
