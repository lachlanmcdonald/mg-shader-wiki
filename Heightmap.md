> The **heightmap** shader treats the first layer of voxels as a 2D height-map texture and extrudes upwards to create a 3D volume. Height is determined by the _perceived luminance_ of each voxel.

<!-- SAMPLE heightmap_usage 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/TODO/heightmap-base.png" alt=""></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/TODO/heightmap-blur-0.png" alt=""></td>
	</tr>
	<tr>
		<td valign="top">Height-map texture</td>
		<td valign="top">Results</td>
	</tr>
</table>
<!-- END -->

<!-- TOC -->
- [Parameters](#parameters)
- [Blur](#blur)
- [Auto Balance](#auto-balance)
- [Reverse](#reverse)

## Parameters

Parameter | Description
--------- | -----------
**Blur**       | Blurs the height-map by the number of voxels to smooth any noise in the original texture. The default value of `0` does not blurring, and values up to `10` increase the blurring and the smoothness of the result.
**Auto Balance**  | When `1`, the range is remapped according to the selected colours in the palette. When `0`, the range is not changed by the palette. See below for more information.
**Reverse**      | When `0`, the luminance of a voxel determines how far it is extruded. When `1`, this is reversed and darker voxels are extruded.

## Blur

<!-- SAMPLE heightmap_blur 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/TODO/heightmap-blur-0.png" alt="Example of a 'Blur' value of 0"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/TODO/heightmap-blur-3.png" alt="Example of a 'Blur' value of 3"></td>
	</tr>
	<tr>
		<th>Blur: <code>0</code></th>
		<th>Blur: <code>3</code></th>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/TODO/heightmap-blur-6.png" alt="Example of a 'Blur' value of 6"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/TODO/heightmap-blur-10.png" alt="Example of a 'Blur' value of 10"></td>
	</tr>
	<tr>
		<th>Blur: <code>6</code></th>
		<th>Blur: <code>10</code></th>
	</tr>
</table>
<!-- END -->

## Auto Balance

<!-- SAMPLE heightmap_autobalance 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/TODO/heightmap-autobalance.png" alt=""></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/TODO/heightmap-autobalance-0.png" alt="Example of a 'Auto Balance' value of 0"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/TODO/heightmap-autobalance-1.png" alt="Example of a 'Auto Balance' value of 1"></td>
	</tr>
	<tr>
		<th></th>
		<th>Auto Balance: <code>0</code></th>
		<th>Auto Balance: <code>1</code></th>
	</tr>
	<tr>
		<td valign="top">Height-map texture</td>
		<td valign="top"></td>
		<td valign="top"></td>
	</tr>
</table>
<!-- END -->

The **heightmap** shader uses the _perceived luminance_ of a voxel to determine its height. By default, the maximum luminance is white (`1.0`) and minimum is black (`0.0`).

 The maximum height is determined by the volume size. 

> If your volume is 20x20x40 voxels, A luminance of `1` would equal `40` voxels; `0.5` would equal `20` voxels; etc.

For instance, if you import a height-map texture that ranges from black (`0.0`) to 50% grey (`0.5`), the heightmap shaders can do two things:

- If **Auto Balance** is `1` and you select the colors in the palette used by the height-map texture, the shader will treat the colours relatively and calculate a new maximum and minimum ranges for you.
- If **Auto Balance** is `0`, the shader will treat values absolutely with no changes, meaning the highest point will be 50% of the volume.

If **Auto Balance** is `1` and you haven't selected ever colour used by the height-map texture, those unselected colours are ignored when generating the map. This can lead to odd results.

## Reverse

<!-- SAMPLE heightmap_reverse 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/TODO/heightmap-reverse0.png" alt="Example of a 'Reverse' value of 0"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/TODO/heightmap-reverse1.png" alt="Example of a 'Reverse' value of 1"></td>
	</tr>
	<tr>
		<th>Reverse: <code>0</code></th>
		<th>Reverse: <code>1</code></th>
	</tr>
</table>
<!-- END -->
