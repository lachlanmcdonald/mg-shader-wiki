> The **tiles_uneven** [brush](Brush-Shaders) generates a uneven pattern of tiles; where the dimensions of the tiles varies.

<!-- TOC -->
- [Arguments](#arguments)
- [Modes](#modes)
- [Thickness](#thickness)
- [Width & Height](#width--height)

## Arguments

Argument | Description
--------- | -----------
**Mode** | Color mode (see below)
**Min** | Minimum tile width and height
**Max** | Maximum tile width and height
**Color A** | Color A
**Color B** | Color B
**Line Color** | Color of the line
**Line Width** | Thickness of the line
**Seed** | Global seed

## Modes

There are 5 distinct color modes for generating patterns, as outlined below:

<!-- SAMPLE tiles_uneven_modes 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/tiles_uneven_mode0.png" alt="Example of a mode of 0"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/tiles_uneven_mode1.png" alt="Example of a mode of 1"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/tiles_uneven_mode2.png" alt="Example of a mode of 2"></td>
	</tr>
	<tr>
		<th>Mode: <code>0</code></th>
		<th>Mode: <code>1</code></th>
		<th>Mode: <code>2</code></th>
	</tr>
	<tr>
		<td valign="top">Tiles are colored at random between <strong>Color A</strong> and <strong>Color B</strong>.</td>
		<td valign="top">Tiles are colored between depending on their size; between <strong>Color A</strong> and <strong>Color B</strong> for small to large, respectively.</td>
		<td valign="top">Tiles are colored at between <strong>Color A</strong> and <strong>Color B</strong> in a repeating sequence.</td>
	</tr>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/tiles_uneven_mode3.png" alt="Example of a mode of 3"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/tiles_uneven_mode4.png" alt="Example of a mode of 4"></td>
	</tr>
	<tr>
		<th>Mode: <code>3</code></th>
		<th>Mode: <code>4</code></th>
	</tr>
	<tr>
		<td valign="top">Tiles are either colored as <strong>Color A</strong> or <strong>Color B</strong> at random.</td>
		<td valign="top">Tiles alternate between <strong>Color A</strong> and <strong>Color B</strong>.</td>
	</tr>
</table>
<!-- END -->

## Thickness

<!-- SAMPLE tiles_uneven_thickness 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/tiles_uneven_thickness0.png" alt="Example of thickness of 0"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/tiles_uneven_thickness1.png" alt="Example of thickness of 1"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/tiles_uneven_thickness2.png" alt="Example of thickness of 2"></td>
	</tr>
	<tr>
		<th>Thickness: <code>0</code></th>
		<th>Thickness: <code>1</code></th>
		<th>Thickness: <code>2</code></th>
	</tr>
</table>
<!-- END -->

## Width & Height

<!-- SAMPLE tiles_uneven_variations 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/tiles_uneven_1x2.png" alt="1x2"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/tiles_uneven_2x4.png" alt="2x4"></td>
	</tr>
	<tr>
		<th><code>1x2</code></th>
		<th><code>2x4</code></th>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/tiles_uneven_4x8.png" alt="4x8"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/tiles_uneven_8x16.png" alt="8x16"></td>
	</tr>
	<tr>
		<th><code>4x8</code></th>
		<th><code>8x16</code></th>
	</tr>
</table>
<!-- END -->
