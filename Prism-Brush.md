> The **Prism [brush](Brush-Shaders)** generates a prism; pyramid or tetrahedron with straight or curved angles.

<!-- TOC -->
- [Arguments](#arguments)
- [Modes](#modes)
- [Widths](#widths)
  - [Mode: `0`](#mode-0)
  - [Mode: `1`](#mode-1)
- [Examples](#examples)

## Arguments

Argument | Description
--------- | -----------
**Mode** | Mode (see below)
**Width X** | Width of the incline on the X-axis (the _step_)
**Width Y** | Width of the incline on the Y-axis (the _step_)

- Setting both a **Width X** and **Width Y** will result in a tetrahedron (or pyryamid)
- Setting either **Width X** or **Width Y** to `0` and the other greater than `0` will result in a prism.
- Setting both to `0` will result in a cube.

## Modes

<!-- SAMPLE prism_modes 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/prism_mode0.png" alt="Example of mode of 0"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/prism_mode1.png" alt="Example of mode of 1"></td>
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

## Widths

### Mode: `0`

<!-- SAMPLE prism_mode0_widths 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/prism_mode0_width8.png" alt="Example of mode of 0 and width 8"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/prism_mode0_width16.png" alt="Example of mode of 0 and width 16"></td>
	</tr>
	<tr>
		<th>Width: <code>8</code></th>
		<th>Width: <code>16</code></th>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/prism_mode0_width20.png" alt="Example of mode of 0 and width 20"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/prism_mode0_width32.png" alt="Example of mode of 0 and width 32"></td>
	</tr>
	<tr>
		<th>Width: <code>20</code></th>
		<th>Width: <code>32</code></th>
	</tr>
</table>
<!-- END -->

### Mode: `1`

<!-- SAMPLE prism_mode1_widths 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/prism_mode1_width8.png" alt="Example of mode of 0 and width 8"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/prism_mode1_width16.png" alt="Example of mode of 0 and width 16"></td>
	</tr>
	<tr>
		<th>Width: <code>8</code></th>
		<th>Width: <code>16</code></th>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/prism_mode1_width20.png" alt="Example of mode of 0 and width 20"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/prism_mode1_width32.png" alt="Example of mode of 0 and width 32"></td>
	</tr>
	<tr>
		<th>Width: <code>20</code></th>
		<th>Width: <code>32</code></th>
	</tr>
</table>
<!-- END -->

## Examples

<!-- SAMPLE prism_examples 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/prism_example0.jpg" alt="Example"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/prism_example1.jpg" alt="Example"></td>
	</tr>
</table>
<!-- END -->
