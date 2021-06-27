> The **Weave [brush](Brush-Shaders)** generates a weave pattern using the selected colors.

<!-- TOC -->
- [Arguments](#arguments)
- [Modes](#modes)
- [Line Width](#line-width)

## Arguments

Argument | Description
--------- | -----------
**Mode** | Color mode (see below)
**Size** | Size of the tiles
**Line Color** | Color index of the outline between tiles
**Line Width** | Width of the outline between tiles
**Seed** | Global seed

## Modes

**Mode** determines how the pattern is colored:

<!-- SAMPLE weave_modes 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/weave_mode_0.png" alt="Example of a 'Mode' value of 0"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/weave_mode_1.png" alt="Example of a 'Mode' value of 1"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/weave_mode_2.png" alt="Example of a 'Mode' value of 2"></td>
	</tr>
	<tr>
		<th>Mode: <code>0</code></th>
		<th>Mode: <code>1</code></th>
		<th>Mode: <code>2</code></th>
	</tr>
	<tr>
		<td valign="top">Tiles are colored at random</td>
		<td valign="top">Tiles are colored in a repeating zig-zag pattern</td>
		<td valign="top">Tiles are alterated between the first and last selected color</td>
	</tr>
</table>
<!-- END -->

## Line Width

<!-- SAMPLE weave_line_widths 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/weave_line_width_0.png" alt="Example of a 'Line Width' value of 0"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/weave_line_width_1.png" alt="Example of a 'Line Width' value of 1"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/weave_line_width_2.png" alt="Example of a 'Line Width' value of 2"></td>
	</tr>
	<tr>
		<th>Line Width: <code>0</code></th>
		<th>Line Width: <code>1</code></th>
		<th>Line Width: <code>2</code></th>
	</tr>
</table>
<!-- END -->
