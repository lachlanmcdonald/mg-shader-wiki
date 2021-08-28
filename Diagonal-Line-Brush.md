> The **Diagonal Line [brush](Brush-Shaders)** generates repeating diagonal (45° lines) of varying thicknesses determined by the selected colors in the palette.

<!-- TOC -->
- [Parameters](#parameters)
- [Directions](#directions)
- [Notes](#notes)

## Parameters

Parameter | Description
--------- | -----------
**Direction** | Direction of the lines on the Z-axis (see below)
**Width A** | Width of the 4-<em>nth</em> line (see below)
**Width B** | Width of the 4-<em>nth</em> + 1 line (see below)
**Width C** | Width of the 4-<em>nth</em> + 2 line (see below)
**Width D** | Width of the 4-<em>nth</em> + 3 line (see below)
**Offset** | Adjusts the offset of the lines
**Shuffle** | Adjusts the colors of the lines

The widths of the lines are independant of the number of selected colours from the palette:

- Up to 4 different widths can be selected.
- If a width is set to `0`, it is skipped from the pattern. For example:
	- widths of `1 0 0 0` is the same as `1 1 1 1`
	- widths of `1 0 2 0` is the same as `1 2 0 0` or `1 2 1 2`
- The colors and line widths repeat over and over, and can be adjusted with the **Shuffle** and **Offset** parameters, respectively.

<!-- SAMPLE diagonal_examples 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/diagonal_1_0_0_0.png" alt=""></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/diagonal_1_2_3_4.png" alt=""></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/diagonal_1_3_0_0.png" alt=""></td>
	</tr>
	<tr>
		<td valign="top">An example of 6 colors and a <strong>Width A</strong> of <code>1</code>, creating a pattern of 6 lines each 1 voxel wide.</td>
		<td valign="top">An example of 2 colors and <strong>Widths</strong> of <code>1</code>, <code>2</code>, <code>3</code>, and <code>4</code>.</td>
		<td valign="top">An example of 6 colors and a <strong>Width A</strong> of <code>1</code> and <strong>Width B</strong> of <code>3</code>, creating a pattern of 6 colors each alternative between 1 and 3 voxels wide.</td>
	</tr>
</table>
<!-- END -->

## Directions

<!-- SAMPLE diagonal_directions 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.4/diagonal3_direction0.png" alt="Example of a 'Direction' value of 0"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.4/diagonal3_direction1.png" alt="Example of a 'Direction' value of 1"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.4/diagonal3_direction2.png" alt="Example of a 'Direction' value of 2"></td>
	</tr>
	<tr>
		<th>Direction: <code>0</code></th>
		<th>Direction: <code>1</code></th>
		<th>Direction: <code>2</code></th>
	</tr>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.4/diagonal3_direction3.png" alt="Example of a 'Direction' value of 3"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.4/diagonal3_direction4.png" alt="Example of a 'Direction' value of 4"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.4/diagonal3_direction5.png" alt="Example of a 'Direction' value of 5"></td>
	</tr>
	<tr>
		<th>Direction: <code>3</code></th>
		<th>Direction: <code>4</code></th>
		<th>Direction: <code>5</code></th>
	</tr>
</table>
<!-- END -->

## Notes

- `diagonal` replaces `diagonal2`, `diagonal3`, and `diagonal_range` from previous releases.
