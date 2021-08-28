> The **truchet [brush](Brush-Shaders)** generates a [truchet tile pattern](https://en.wikipedia.org/wiki/Truchet_tiles) using the selected colors.

<!-- TOC -->
- [Parameters](#parameters)
- [Modes](#modes)
- [Size](#size)
- [Noise](#noise)

## Parameters

Parameter | Description
--------- | -----------
**Mode** | Color mode (see below)
**Size** | Size of the tiles (tilse are always square)
**Noise** | Additional color noise on each tile
**Seed** | Global seed 

## Modes

<!-- SAMPLE truchet_mode 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/truchet_mode0_compressed.jpg" alt="Example of a 'Mode' value of 0"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/truchet_mode1_compressed.jpg" alt="Example of a 'Mode' value of 1"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/truchet_mode2_compressed.jpg" alt="Example of a 'Mode' value of 2"></td>
	</tr>
	<tr>
		<th>Mode: <code>0</code></th>
		<th>Mode: <code>1</code></th>
		<th>Mode: <code>2</code></th>
	</tr>
	<tr>
		<td valign="top">Tiles are colored in pairs</td>
		<td valign="top">Tiles are colored randomly</td>
		<td valign="top">Tiles are colored randomly (in reverse)</td>
	</tr>
</table>
<!-- END -->

## Size

<!-- SAMPLE truchet_size 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/truchet_size5_compressed.jpg" alt="Example of a 'Size' value of 5"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/truchet_size10_compressed.jpg" alt="Example of a 'Size' value of 10"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/truchet_size20_compressed.jpg" alt="Example of a 'Size' value of 20"></td>
	</tr>
	<tr>
		<th>Size: <code>5</code></th>
		<th>Size: <code>10</code></th>
		<th>Size: <code>20</code></th>
	</tr>
</table>
<!-- END -->

## Noise

<!-- SAMPLE truchet_noise 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/truchet_noise0_compressed.jpg" alt="Example of a 'Noise' value of 0"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/truchet_noise15_compressed.jpg" alt="Example of a 'Noise' value of 15"></td>
	</tr>
	<tr>
		<th>Noise: <code>0</code></th>
		<th>Noise: <code>15</code></th>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/truchet_noise40_compressed.jpg" alt="Example of a 'Noise' value of 40"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/truchet_noise50_compressed.jpg" alt="Example of a 'Noise' value of 50"></td>
	</tr>
	<tr>
		<th>Noise: <code>40</code></th>
		<th>Noise: <code>50</code></th>
	</tr>
</table>
<!-- END -->
