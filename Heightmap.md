> The **heightmap** shader treats the first layer of voxels as a 2D height-map texture and extrudes upwards to create a 3D volume. The height is determined by the [_relative luminance_](https://en.wikipedia.org/wiki/Relative_luminance) of each voxel.

<!-- TOC -->
- [Parameters](#parameters)
  - [Blur](#blur)
  - [Auto Balance](#auto-balance)
  - [Reverse](#reverse)
- [Examples](#examples)

## Parameters

Parameter | Description
--------- | -----------
**Blur** | Blurs the height-map by the number of voxels specified. Used to smoothes any noise in the original texture. The default value of `0` does not blur, and values up to `10` increase the blurring and the smoothness of the result.
**Auto Balance** | When `1`, the range is remapped according to the selected colors in the palette. When `0`, the range is not changed by the palette. See below for more information.
**Reverse** | When `0`, the luminance of a voxel determines how far it is extruded. When `1`, this is reversed and darker voxels are extruded instead.

### Blur

<!-- SAMPLE heightmap blur 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/heightmap-blur0.png" alt="Example of a 'Blur' value of 0"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/heightmap-blur3.png" alt="Example of a 'Blur' value of 3"></td>
	</tr>
	<tr>
		<th>Blur: <code>0</code></th>
		<th>Blur: <code>3</code></th>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/heightmap-blur6.png" alt="Example of a 'Blur' value of 6"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/heightmap-blur10.png" alt="Example of a 'Blur' value of 10"></td>
	</tr>
	<tr>
		<th>Blur: <code>6</code></th>
		<th>Blur: <code>10</code></th>
	</tr>
</table>
<!-- END -->

### Auto Balance

<!-- SAMPLE heightmap autobalance 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/heightmap-autobalance.png" alt=""></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/heightmap-autobalance0.png" alt="Example of a 'Auto Balance' value of 0"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/heightmap-autobalance1.png" alt="Example of a 'Auto Balance' value of 1"></td>
	</tr>
	<tr>
		<th></th>
		<th>Auto Balance: <code>0</code></th>
		<th>Auto Balance: <code>1</code></th>
	</tr>
</table>
<!-- END -->

The **heightmap** shader uses the [_relative luminance_](https://en.wikipedia.org/wiki/Relative_luminance) of a voxel to determine its height. By default, the maximum luminance is white (`1.0`) and minimum is black (`0.0`).

 The maximum height is determined by the volume size. 

For example, if you import a height-map texture that ranges from black (`0.0`) to 50% grey (`0.5`), the heightmap shaders can do two things:

- If **Auto Balance** is `1` and you select the colors in the palette used by the height-map texture, the shader will treat the colors relatively and calculate a new maximum and minimum ranges for you.
- If **Auto Balance** is `0`, the shader will treat values absolutely (no changes), meaning the highest point will be 50% of the volume.

If **Auto Balance** is `1`, any unselected colors that were used by the texture are ignored when generating the volume. This can lead to odd results.

### Reverse

<!-- SAMPLE heightmap reverse 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/heightmap-reverse0.png" alt="Example of a 'Reverse' value of 0"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/heightmap-reverse1.png" alt="Example of a 'Reverse' value of 1"></td>
	</tr>
	<tr>
		<th>Reverse: <code>0</code></th>
		<th>Reverse: <code>1</code></th>
	</tr>
</table>
<!-- END -->

## Examples

<!-- SAMPLE heightmap usage 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/heightmap-base.png" alt=""></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/heightmap-blur0.png" alt=""></td>
	</tr>
	<tr>
		<td valign="top">Height-map texture</td>
		<td valign="top">Results</td>
	</tr>
</table>
<!-- END -->
