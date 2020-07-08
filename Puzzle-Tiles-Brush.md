> The **tiles_puzzle** [brush](Brush-Shaders) generates a puzzle-like pattern of tiles.

<!-- TOC -->
- [Arguments](#arguments)
- [Modes](#modes)
- [Line Widths](#line-widths)
- [Examples](#examples)

## Arguments

Argument | Description
--------- | -----------
**Mode** | Color mode (see below)
**Color A** | Color A
**Color B** | Color B
**Size X** | Tile width
**Size Y** | Tile height
**Line Color** | Color of the line
**Line Width** | Thickness of the line
**Seed** | Global seed

## Modes

There are 5 distinct color modes for generating patterns, as outlined below:

<!-- SAMPLE tiles_puzzle_modes 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/tiles_puzzle_mode0.png" alt="Example of a mode of 0"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/tiles_puzzle_mode1.png" alt="Example of a mode of 1"></td>
	</tr>
	<tr>
		<th>Mode: <code>0</code></th>
		<th>Mode: <code>1</code></th>
	</tr>
	<tr>
		<td valign="top">Tiles are colored at random between <strong>Color A</strong> and <strong>Color B</strong>.</td>
		<td valign="top">Tiles are either colored as <strong>Color A</strong> or <strong>Color B</strong>.</td>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/tiles_puzzle_mode2.png" alt="Example of a mode of 2"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/tiles_puzzle_mode3.png" alt="Example of a mode of 3"></td>
	</tr>
	<tr>
		<th>Mode: <code>2</code></th>
		<th>Mode: <code>3</code></th>
	</tr>
	<tr>
		<td valign="top">Similar to mode <code>0</code>, only tiles directed towards the X axis are randomly colored. Remaining tiles become <strong>Line Color</strong>.</td>
		<td valign="top">Similar to mode <code>0</code>, only tiles directed towards the Y axis are randomly colored. Remaining tiles become <strong>Line Color</strong>.</td>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/tiles_puzzle_mode4.png" alt="Example of a mode of 4"></td>
	</tr>
	<tr>
		<th>Mode: <code>4</code></th>
	</tr>
	<tr>
		<td valign="top">Tiles are colored at random between <strong>Color A</strong> and <strong>Color B</strong>. Tiles directed towards the X axis selected from the first half of the <strong>color r</strong>ange, and Y axis the selected from the second half of the <strong>color r</strong>ange.</td>
	</tr>
</table>
<!-- END -->

## Line Widths

<!-- SAMPLE tiles_puzzle_line_widths 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/tiles_puzzle_line_width0.png" alt="Example of line width of 0"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/tiles_puzzle_line_width1.png" alt="Example of line width of 1"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/tiles_puzzle_line_width2.png" alt="Example of line width of 2"></td>
	</tr>
	<tr>
		<th>Line Width: <code>0</code></th>
		<th>Line Width: <code>1</code></th>
		<th>Line Width: <code>2</code></th>
	</tr>
</table>
<!-- END -->

## Examples

<!-- SAMPLE tiles_puzzle_examples 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/tiles_puzzle_example0.jpg" alt="Example"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/tiles_puzzle_example1.jpg" alt="Example"></td>
	</tr>
</table>
<!-- END -->

