> The **`prism`** [primitive brush](Brush-Shaders) generates a prism; pyramid or tetrahedron with straight or curved angles.

<!-- TOC -->
- [Parameters](#parameters)
- [Modes](#modes)
- [Sizes](#sizes)
  - [Mode: `0`](#mode-0)
  - [Mode: `1`](#mode-1)
- [Examples](#examples)

## Parameters

Parameter | Description
--------- | -----------
**Mode** | Mode (see below)
**Size X** | Size of the incline on the X-axis (the _step_)
**Size Y** | Size of the incline on the Y-axis (the _step_)

- Setting both a **Size X** and **Size Y** will result in a tetrahedron (or pyryamid)
- Setting either **Size X** or **Size Y** to `0` and the other greater than `0` will result in a prism.
- Setting both to `0` will result in a cube.

## Modes

<!-- SAMPLE prism_modes 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/prism_mode0.png" alt="Example of a 'Mode' value of 0"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/prism_mode1.png" alt="Example of a 'Mode' value of 1"></td>
	</tr>
	<tr>
		<th>Mode: <code>0</code></th>
		<th>Mode: <code>1</code></th>
	</tr>
	<tr>
		<td valign="top">Linear interpolation (straight edge)</td>
		<td valign="top">Sine interpolation (curved edge)</td>
	</tr>
</table>
<!-- END -->

## Mode: `0`

<!-- SAMPLE prism_mode0_sizes 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/prism_mode0_width8.png" alt="Example of mode of 0 and size 8"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/prism_mode0_width16.png" alt="Example of mode of 0 and size 16"></td>
	</tr>
	<tr>
		<th>Size: <code>8</code></th>
		<th>Size: <code>16</code></th>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/prism_mode0_width20.png" alt="Example of mode of 0 and size 20"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/prism_mode0_width32.png" alt="Example of mode of 0 and size 32"></td>
	</tr>
	<tr>
		<th>Size: <code>20</code></th>
		<th>Size: <code>32</code></th>
	</tr>
</table>
<!-- END -->

## Mode: `1`

<!-- SAMPLE prism_mode1_sizes 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/prism_mode1_width8.png" alt="Example of mode of 0 and size 8"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/prism_mode1_width16.png" alt="Example of mode of 0 and size 16"></td>
	</tr>
	<tr>
		<th>Size: <code>8</code></th>
		<th>Size: <code>16</code></th>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/prism_mode1_width20.png" alt="Example of mode of 0 and size 20"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/prism_mode1_width32.png" alt="Example of mode of 0 and size 32"></td>
	</tr>
	<tr>
		<th>Size: <code>20</code></th>
		<th>Size: <code>32</code></th>
	</tr>
</table>
<!-- END -->

## Examples

<!-- SAMPLE prism_examples 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/prism_example0.jpg" alt=""></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/prism_example1.jpg" alt=""></td>
	</tr>
</table>
<!-- END -->
