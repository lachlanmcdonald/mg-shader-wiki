> **noise** replaces all voxels which match a specified color with a randomly chosen color from the selected colors in the palette.
> 
> See also the [Random](Random) shader and the [Noise brush shaders](Noise-Brushes).

<!-- TOC -->
- [Parameters](#parameters)
  - [Sizes](#sizes)
- [Axis Modes](#axis-modes)

## Parameters

Parameter | Description
--------- | -----------
**Target Color** | Color index to replace
**Size X** | Size of the noise on the X-axis
**Size Y** | Size of the noise on the Y-axis
**Size Z** | Size of the noise on the Z-axis
**Seed** | Global seed

### Sizes

<!-- SAMPLE noise sizes 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/noise_size_1_1_1.png" alt="Example of a size of 1x1x1"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/noise_size_2_2_8.png" alt="Example of a size of 2x2x8"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/noise_size_4_10_1.png" alt="Example of a size of 4x10x1"></td>
	</tr>
	<tr>
		<th>Example of a size of 1x1x1</th>
		<th>Example of a size of 2x2x8</th>
		<th>Example of a size of 4x10x1</th>
	</tr>
</table>
<!-- END -->

## Axis Modes

Axis modes can use used to only add noise on certain axes:

<!-- SAMPLE noise axis 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/noise_no_axis.png" alt="Example of no set axis mode"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/noise_no_axis.png" alt="Example of X-axis mode"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/noise_xy_axis.png" alt="Example of X &amp; Y-axis mode"></td>
	</tr>
	<tr>
		<th>No set axis mode</th>
		<th>X-axis mode</th>
		<th>X &amp; Y-axis mode</th>
	</tr>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/noise_y_axis.png" alt="Example of Y-axis mode"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/noise_z_axis.png" alt="Example of Z-axis mode"></td>
	</tr>
	<tr>
		<th>Y-axis mode</th>
		<th>Z-axis mode</th>
	</tr>
</table>
<!-- END -->
