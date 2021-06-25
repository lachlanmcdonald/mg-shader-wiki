> **greebles2** is a **[greeble brush](Greeble-Brushes)** that generates greebles by randomly generating an uneven grid and then randomly intruding each cell.

<!-- TOC -->
- [Arguments](#arguments)
- [Modes](#modes)
- [Axis Modes](#axis-modes)
- [Width, Height & Depth](#width-height--depth)

## Arguments

Argument | Description
--------- | -----------
**Mode** | Mode (see below)
**Min** | Minimum cell size
**Max** | Maximum cell size
**Depth** | Maximum depth
**Seed** | Global seed


## Modes

<!-- SAMPLE greebles2_modes 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/greebles2_mode0.jpg" alt="Example of mode 0"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/greebles2_mode1.jpg" alt="Example of mode 1"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/greebles2_mode2.jpg" alt="Example of mode 2"></td>
	</tr>
	<tr>
		<th>Mode</th>
		<th>Mode: <code>1</code></th>
		<th>Mode: <code>2</code></th>
	</tr>
	<tr>
		<td valign="top">Cells are intruded from the surface</td>
		<td valign="top">Cells are added instead of intruded, creating a hollow shell</td>
		<td valign="top">Only cells at the edges are removed</td>
	</tr>
</table>
<!-- END -->

## Axis Modes

Axis modes can use used to only add cuboids on certain axes.

<!-- SAMPLE greebles2_axis 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/greebles2_axis_x.jpg" alt="Example of X-axis mode"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/greebles2_axis_y.jpg" alt="Example of Y-axis mode"></td>
	</tr>
	<tr>
		<th>X-axis mode</th>
		<th>Y-axis mode</th>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/greebles2_axis_xy.jpg" alt="Example of X &amp; Y-axis mode"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/greebles2_axis_z.jpg" alt="Example of Z-axis mode"></td>
	</tr>
	<tr>
		<th>X &amp; Y-axis mode</th>
		<th>Z-axis mode</th>
	</tr>
</table>
<!-- END -->

## Width, Height & Depth

<!-- SAMPLE greebles2_variations 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/greebles2_axis_1x3x4.jpg" alt="1x3x4"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/greebles2_axis_4x4x4.jpg" alt="4x4x4"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/greebles2_axis_mode2_4x1x7.jpg" alt="4x1x7"></td>
	</tr>
	<tr>
		<th><code>1x3x4</code></th>
		<th><code>4x4x4</code></th>
		<th><code>4x1x7</code></th>
	</tr>
</table>
<!-- END -->
