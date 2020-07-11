> The **Weave [brush](Brush-Shaders)** generates a weave pattern.

<!-- TOC -->
- [Arguments](#arguments)
- [Modes](#modes)
- [Line Width](#line-width)

## Arguments

Argument | Description
--------- | -----------
**Mode** | Color mode (see below)
**Size** | Size of the squares
**Color A** | First color index
**Color B** | Last color index
**Line Color** | Color index of the outline between squares
**Line Width** | Width of the outline between squares

Setting either of the colors to `0` will result in empty voxels.

## Modes

**Mode** determines how the pattern is colored:

<!-- SAMPLE weave_modes 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.0/wave_mode_0.png" alt="Example of mode of 0"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.0/wave_mode_1.png" alt="Example of mode of 1"></td>
	</tr>
	<tr>
		<th>Mode: <code>0</code></th>
		<th>Mode: <code>1</code></th>
	</tr>
	<tr>
		<td valign="top">Squares are colored at random</td>
		<td valign="top">Squares alternate color</td>
	</tr>
</table>
<!-- END -->

## Line Width

<!-- SAMPLE weave_line_widths 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.0/weave_line_width_0.png" alt="Example of a Line Width of 0"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.0/weave_line_width_1.png" alt="Example of a Line Width of 1"></td>
	</tr>
	<tr>
		<th>Line Width: <code>0</code></th>
		<th>Line Width: <code>1</code></th>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.0/weave_line_width_2.png" alt="Example of a Line Width of 2"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.0/weave_line_width_3.png" alt="Example of a Line Width of 3"></td>
	</tr>
	<tr>
		<th>Line Width: <code>2</code></th>
		<th>Line Width: <code>3</code></th>
	</tr>
</table>
<!-- END -->
