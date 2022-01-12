> The **`grid`** [brush](Brush-Shaders) generates a grid pattern with variable thickness and spacing.

<!-- TOC -->
- [Parameters](#parameters)
  - [Thickness](#thickness)
- [Axis Modes](#axis-modes)
- [Examples](#examples)

## Parameters

Parameter | Description
--------- | -----------
**Color A** | Color index of the lines
**Color B** | Color index of the boxes in between the lines
**Thickness** | Line thickness
**Size X** | Spacing between lines on the X-axis
**Size Y** | Spacing between lines on the Y-axis
**Size Z** | Spacing between lines on the Z-axis

Setting **Color A** to `0` will result in gaps, instead of lines. Similarly, setting **Color B** to `0` will only produce lines (with no boxes in between).

### Thickness

<!-- SAMPLE grid thickness 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/5efad020-561b-4086-866d-40868862311e/grid_thickness_1.png" alt="Example of a 'Thickness' value of 1"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/5efad020-561b-4086-866d-40868862311e/grid_thickness_2.png" alt="Example of a 'Thickness' value of 2"></td>
	</tr>
	<tr>
		<th>Thickness: <code>1</code></th>
		<th>Thickness: <code>2</code></th>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/5efad020-561b-4086-866d-40868862311e/grid_thickness_3.png" alt="Example of a 'Thickness' value of 3"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/5efad020-561b-4086-866d-40868862311e/grid_thickness_4.png" alt="Example of a 'Thickness' value of 4"></td>
	</tr>
	<tr>
		<th>Thickness: <code>3</code></th>
		<th>Thickness: <code>4</code></th>
	</tr>
</table>
<!-- END -->

## Axis Modes

[Axis Modes](Terms#axis-modes) can use used ensure voxels are only generated on certain axes:

<!-- SAMPLE grid axis 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/5efad020-561b-4086-866d-40868862311e/magica_grid_axis_XYZ.png" alt="Example of no set axis mode"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/5efad020-561b-4086-866d-40868862311e/magica_grid_axis_X.png" alt="Example of X-axis mode"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/5efad020-561b-4086-866d-40868862311e/magica_grid_axis_Y.png" alt="Example of Y-axis mode"></td>
	</tr>
	<tr>
		<th>No set axis mode</th>
		<th>X-axis mode</th>
		<th>Y-axis mode</th>
	</tr>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/5efad020-561b-4086-866d-40868862311e/magica_grid_axis_XY.png" alt="Example of X &amp; Y-axis mode"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/5efad020-561b-4086-866d-40868862311e/magica_grid_axis_Z.png" alt="Example of Z-axis mode"></td>
	</tr>
	<tr>
		<th>X &amp; Y-axis mode</th>
		<th>Z-axis mode</th>
	</tr>
</table>
<!-- END -->

## Examples

<!-- SAMPLE grid examples 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/magica_grid_1.png" alt=""></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/magica_grid_2.png" alt=""></td>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/magica_grid_3.png" alt=""></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/magica_grid_4.png" alt=""></td>
	</tr>
</table>
<!-- END -->
