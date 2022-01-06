> The **`tiles_uneven`** [brush](Brush-Shaders) generates a uneven pattern of tiles; where the dimensions of the tiles varies.

<!-- TOC -->
- [Parameters](#parameters)
- [Modes](#modes)
- [Min & Max](#min--max)
- [Line Width](#line-width)
- [Noise](#noise)

## Parameters

Parameter | Description
--------- | -----------
**Mode** | Color mode (see below)
**Min** | Minimum tile width and height
**Max** | Maximum tile width and height
**Line Color** | Color of the line
**Line Width** | Thickness of the line
**Noise** | Randomness of the colors within each tile. Values closer to `0` produce solid colored tiles, where as values closer to `1` produce noisy tiles (see below)
**Seed** | Global seed

## Modes

There are 5 distinct color modes for generating patterns, as outlined below:

<!-- SAMPLE tiles_uneven modes 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/tiles_uneven_mode_0.png" alt="Example of a 'Mode' value of 0"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/tiles_uneven_mode_1.png" alt="Example of a 'Mode' value of 1"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/tiles_uneven_mode_2.png" alt="Example of a 'Mode' value of 2"></td>
	</tr>
	<tr>
		<th>Mode: <code>0</code></th>
		<th>Mode: <code>1</code></th>
		<th>Mode: <code>2</code></th>
	</tr>
	<tr>
		<td valign="top">Tiles are colored at random between the selected colors.</td>
		<td valign="top">Tiles are colored between depending on their size between the selected colors.</td>
		<td valign="top">Tiles are colored between the selected colors in a repeating pattern along the X-axis</td>
	</tr>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/tiles_uneven_mode_3.png" alt="Example of a 'Mode' value of 3"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/tiles_uneven_mode_4.png" alt="Example of a 'Mode' value of 4"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/tiles_uneven_mode_5.png" alt="Example of a 'Mode' value of 5"></td>
	</tr>
	<tr>
		<th>Mode: <code>3</code></th>
		<th>Mode: <code>4</code></th>
		<th>Mode: <code>5</code></th>
	</tr>
	<tr>
		<td valign="top">Tiles are colored between the selected colors in a repeating pattern along the Y-axis</td>
		<td valign="top">Tiles are colored at random using only the first and last selected color</td>
		<td valign="top">Tiles are colored in an alternating pattern using only the first and last selected color</td>
	</tr>
</table>
<!-- END -->

## Min & Max

<!-- SAMPLE tiles_uneven variations 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/tiles_uneven_2x4.png" alt="Example of a '' value of 2x4"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/tiles_uneven_2x12.png" alt="Example of a '' value of 2x12"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/tiles_uneven_4x8.png" alt="Example of a '' value of 4x8"></td>
	</tr>
	<tr>
		<th><code>2x4</code></th>
		<th><code>2x12</code></th>
		<th><code>4x8</code></th>
	</tr>
</table>
<!-- END -->

## Line Width

<!-- SAMPLE tiles_uneven line_width 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/tiles_uneven_line_0.png" alt="Example of a 'Line Width' value of 0"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/tiles_uneven_line_1.png" alt="Example of a 'Line Width' value of 1"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/tiles_uneven_line_2.png" alt="Example of a 'Line Width' value of 2"></td>
	</tr>
	<tr>
		<th>Line Width: <code>0</code></th>
		<th>Line Width: <code>1</code></th>
		<th>Line Width: <code>2</code></th>
	</tr>
</table>
<!-- END -->

## Noise

<!-- SAMPLE tiles_uneven noise 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/tiles_uneven_noise_0.png" alt="Example of a 'Noise' value of 0"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/tiles_uneven_noise_25.png" alt="Example of a 'Noise' value of 25"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/tiles_uneven_noise_50.png" alt="Example of a 'Noise' value of 50"></td>
	</tr>
	<tr>
		<th>Noise: <code>0</code></th>
		<th>Noise: <code>25</code></th>
		<th>Noise: <code>50</code></th>
	</tr>
	<tr>
		<td valign="top">Tiles are colored at random between the selected colors.</td>
		<td valign="top">Tiles are colored between depending on their size between the selected colors.</td>
		<td valign="top">Tiles are colored between the selected colors in a repeating pattern along the X-axis</td>
	</tr>
</table>
<!-- END -->
