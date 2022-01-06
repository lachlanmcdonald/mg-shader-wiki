> The **`tiles_puzzle`** [brush](Brush-Shaders) generates a puzzle-like pattern of tiles.

<!-- TOC -->
- [Parameters](#parameters)
- [Modes](#modes)
- [Size X & Y](#size-x--y)
- [Line Width](#line-width)
- [Noise](#noise)
- [Examples](#examples)

## Parameters

Parameter | Description
--------- | -----------
**Mode** | Color mode (see below)
**Size X** | Tile width
**Size Y** | Tile height
**Line Color** | Color of the line
**Line Width** | Thickness of the line
**Noise** | Randomness of the colors within each tile. Values closer to `0` produce solid colored tiles, where as values closer to `1` produce noisy tiles (see below)
**Seed** | Global seed

## Modes

There are 5 distinct color modes for generating patterns:

<!-- SAMPLE tiles_puzzle mode 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/tiles_puzzle_mode_0.png" alt="Example of a 'Mode' value of 0"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/tiles_puzzle_mode_1.png" alt="Example of a 'Mode' value of 1"></td>
	</tr>
	<tr>
		<th>Mode: <code>0</code></th>
		<th>Mode: <code>1</code></th>
	</tr>
	<tr>
		<td valign="top">Tiles are colored at random between the selected colors.</td>
		<td valign="top">Tiles are colored at random using only the first and last selected color.</td>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/tiles_puzzle_mode_2.png" alt="Example of a 'Mode' value of 2"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/tiles_puzzle_mode_3.png" alt="Example of a 'Mode' value of 3"></td>
	</tr>
	<tr>
		<th>Mode: <code>2</code></th>
		<th>Mode: <code>3</code></th>
	</tr>
	<tr>
		<td valign="top">Similar to mode <code>0</code>, but only tiles directed towards the X-axis are colored. Remaining tiles become <strong>Line Color</strong>.</td>
		<td valign="top">Similar to mode <code>0</code>, but only tiles directed towards the Y-axis are colored. Remaining tiles become <strong>Line Color</strong>.</td>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/tiles_puzzle_mode_4.png" alt="Example of a 'Mode' value of 4"></td>
	</tr>
	<tr>
		<th>Mode: <code>4</code></th>
	</tr>
	<tr>
		<td valign="top">Similar to mode <code>0</code>, but tiles directed towards the X-axis selected from the first half of the selected colors, and Y-axis the selected from the second half of the selected colours.</td>
	</tr>
</table>
<!-- END -->

## Size X & Y

<!-- SAMPLE tiles_puzzle variations 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/tiles_puzzle_4x4.png" alt="Example of a '' value of 4x4"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/tiles_puzzle_2x8.png" alt="Example of a '' value of 2x8"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/tiles_puzzle_8x8.png" alt="Example of a '' value of 8x8"></td>
	</tr>
	<tr>
		<th><code>4x4</code></th>
		<th><code>2x8</code></th>
		<th><code>8x8</code></th>
	</tr>
</table>
<!-- END -->

## Line Width

<!-- SAMPLE tiles_puzzle line_width 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/tiles_puzzle_line_0.png" alt="Example of a 'Line Width' value of 0"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/tiles_puzzle_line_1.png" alt="Example of a 'Line Width' value of 1"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/tiles_puzzle_line_2.png" alt="Example of a 'Line Width' value of 2"></td>
	</tr>
	<tr>
		<th>Line Width: <code>0</code></th>
		<th>Line Width: <code>1</code></th>
		<th>Line Width: <code>2</code></th>
	</tr>
</table>
<!-- END -->

## Noise

<!-- SAMPLE tiles_puzzle noise 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/tiles_puzzle_noise_0.png" alt="Example of a 'Noise' value of 0"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/tiles_puzzle_noise_25.png" alt="Example of a 'Noise' value of 25"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/tiles_puzzle_noise_50.png" alt="Example of a 'Noise' value of 50"></td>
	</tr>
	<tr>
		<th>Noise: <code>0</code></th>
		<th>Noise: <code>25</code></th>
		<th>Noise: <code>50</code></th>
	</tr>
</table>
<!-- END -->

## Examples

<!-- SAMPLE tiles_puzzle examples 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/tiles_puzzle_example0.jpg" alt="Example"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/tiles_puzzle_example1.jpg" alt="Example"></td>
	</tr>
</table>
<!-- END -->
