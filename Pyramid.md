> The **`pyramid`** shader add a layer of voxel on top of voxels matching the selected colors. A voxel is only added when the voxel beneath has adjacent voxels, creating the effect of a pyramid.

<!-- TOC -->
- [Parameters](#parameters)
- [Axis Modes](#axis-modes)
  - [Noise](#noise)
- [Notes](#notes)

## Parameters

Voxels are added on top of voxels matching the selected colors. The color of the new voxel matches the voxel beneath, but this can be varied with the *Noise* parameter.

Parameter | Description
--------- | -----------
**Noise** | Amount of randomness to introduce when picking a color for new voxels. When `0`, the new voxel will match the color of the voxel underneath. Values closer to `100` will increase the chance the voxel color is chosen at random from the selected colors.
**Seed** | Global seed

## Axis Modes

When no [Axis Modes](Terms#axis-modes) are set, the shader will form a square pyramid. However, if either X or Y-Axis Modes are set, the shader will form a pyramid with the slope facing the X or Y axis, respectively. Setting the Z-axis mode has no effect.

<!-- SAMPLE pyramid axis 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/pyramid_rect.png" alt=""></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/pyramid_rect_no_axis.png" alt=""></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/pyramid_rect_x.png" alt=""></td>
	</tr>
	<tr>
		<td valign="top">Original</td>
		<td valign="top">No axis mode</td>
		<td valign="top">X-axis mode</td>
	</tr>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/pyramid_circle.png" alt=""></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/pyramid_circle_no_axis.png" alt=""></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/pyramid_circle_x_axis.png" alt=""></td>
	</tr>
	<tr>
		<td valign="top">Original</td>
		<td valign="top">No axis mode</td>
		<td valign="top">X-axis mode</td>
	</tr>
</table>
<!-- END -->

### Noise

Noise will accumulate. For example, for a value of `0.1`, the original pattern is almost completely lost after 10 iterations.

<!-- SAMPLE pyramid noise 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/pyramid_noise_0.png" alt="Example of a 'Noise' value of 0"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/pyramid_noise_50.png" alt="Example of a 'Noise' value of 50"></td>
	</tr>
	<tr>
		<th>Noise: <code>0</code></th>
		<th>Noise: <code>50</code></th>
	</tr>
</table>
<!-- END -->

## Notes

- `pyramid2` has been removed as it is no longer as useful with multiple volumes/World feature.
