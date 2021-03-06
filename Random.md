> **random** replaces voxels which match the selected colors, at random, with a chosen color.
> 
> See also the [Noise](Noise) shader and the [Noise brush shaders](Noise-Brushes).

<!-- TOC -->
- [Parameters](#parameters)
  - [Threshold](#threshold)
- [Axis Modes](#axis-modes)

## Parameters

Parameter | Description
--------- | -----------
**Threshold** | Threshold of noise, lower values produce replace less voxels and higher values replace more voxels
**Color** | Color index to replace voxels (setting the index to `0` will remove voxels)

### Threshold

<table>
    <tr>
        <td width="33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/rand_025.png" alt=""></td>
        <td width="33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/rand_050.png" alt=""></td>
        <td width="33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/rand_075.png" alt=""></td>
    </tr>
	<tr>
		<th>Threshold: <code>25</code></th>
		<th>Threshold: <code>50</code></th>
		<th>Threshold: <code>75</code></th>
	</tr>
</table>

## Axis Modes

By default, voxels are replaced across all axes. But this can be restricted to the X, Y, or Z-axis (or a combination) with the axis modes:

<table>
    <tr>
        <td width="33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/rand_050_y.png" alt=""></td>
        <td width="33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/rand_050_xy.png" alt=""></td>
        <td width="33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/rand_050_xz.png" alt=""></td>
    </tr>
	<tr>
		<th>Y-axis</th>
		<th>X &amp; Y axes</th>
		<th>X &amp; Z axes</th>
	</tr>
</table>
