> The **`erode`** shader randomly removes the surface voxels from your volume based on a 3D noise texture, giving the impression of erosion and damage.
> 
> This shader only removes voxels that match the selected colors from the palette.

<!-- TOC -->
- [Parameters](#parameters)
- [Example](#example)
- [Threshold](#threshold)
- [Scale](#scale)
- [Seed](#seed)

## Parameters

Parameter | Description
--------- | -----------
**Threshold** | Limits the erosion to voxels with a certain number of neighbours. See below for more information.
**Scale** | Size of erosion texture. Larger values producer smaller clusters of erotion.
**Seed**   | Global seed

> The seed is automatically randomised when on each iteration.

## Example

<!-- SAMPLE erode exmaples 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/erosion_base.jpg" alt=""></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/erosion_scale6.jpg" alt=""></td>
	</tr>
	<tr>
		<td valign="top">Befrore</td>
		<td valign="top">After</td>
	</tr>
</table>
<!-- END -->

## Threshold

Each voxel has 26 neighbouring voxels:

- The default **Threshold** of `9` will include voxels with at least nine empty neighbours (for instance, the outside layer of a wall).
- A **Threshold** of `1` will include any voxels with at least one empty neighbour, which includes all voxels besides those surrounded by other voxels.

<!-- SAMPLE erode threshold 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/erosion_threshold1.jpg" alt="Example of a 'Threshold' value of 1"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/erosion_threshold18.jpg" alt="Example of a 'Threshold' value of 18"></td>
	</tr>
	<tr>
		<th>Threshold: <code>1</code></th>
		<th>Threshold: <code>18</code></th>
	</tr>
</table>
<!-- END -->

## Scale

<!-- SAMPLE erode scale 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/erosion_scale3.jpg" alt="Example of a 'Scale' value of 3"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/erosion_scale6.jpg" alt="Example of a 'Scale' value of 6"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/erosion_scale20.jpg" alt="Example of a 'Scale' value of 20"></td>
	</tr>
	<tr>
		<th>Scale: <code>3</code></th>
		<th>Scale: <code>6</code></th>
		<th>Scale: <code>20</code></th>
	</tr>
</table>
<!-- END -->

## Seed

The **Seed** affects the generation of the 3D noise used to erode the volume. However, unless you update the **Seed** each time you run the shader, the same texture will continue to be used. However, when the shader is run with _Iterations_, the Seed is updated automatically.

<!-- SAMPLE erode iterations 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/erosions_runs4.jpg" alt=""></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/erosion_iterations4.jpg" alt=""></td>
	</tr>
	<tr>
		<td valign="top">The shader run 4 times</td>
		<td valign="top">The shader run with 4 iterations</td>
	</tr>
</table>
<!-- END -->
