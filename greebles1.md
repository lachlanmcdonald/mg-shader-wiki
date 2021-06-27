> **greebles1** is a **[greeble brush](Greeble-Brushes)** that generates greebles by randomly generating cuboids and subtracting voxels that overlap.

<!-- TOC -->
- [Arguments](#arguments)
- [Modes](#modes)
- [Axis Modes](#axis-modes)
- [Count](#count)
- [Width, Height & Depth](#width-height--depth)
- [Examples](#examples)

## Arguments

Argument | Description
--------- | -----------
**Mode** | Mode (see below)
**Count** | Number of cuboids to generate (higher values results in more greebles)
**Width** | Maximum width of the randomly generated cuboids
**Height** | Maximum height of the randomly generated cuboids
**Depth** | Maximum depth of the randomly generated cuboids
**Seed** | Global seed

## Modes

<!-- SAMPLE greebles1_modes 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/greebles1_mode0.jpg" alt=""></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/greebles1_mode1.jpg" alt="Example of a 'Mode' value of 1"></td>
	</tr>
	<tr>
		<th>Mode</th>
		<th>Mode: <code>1</code></th>
	</tr>
	<tr>
		<td valign="top">Voxels overlapping cuboids are removed</td>
		<td valign="top">Only voxels overlapping cuboids are kept</td>
	</tr>
</table>
<!-- END -->

## Axis Modes

Axis modes can use used to only add cuboids on certain axes.

<!-- SAMPLE greebles1_axis 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/greebles1_axis_x.jpg" alt="Example of X-axis mode"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/greebles1_axis_y.jpg" alt="Example of Y-axis mode"></td>
	</tr>
	<tr>
		<th>X-axis mode</th>
		<th>Y-axis mode</th>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/greebles1_axis_xy.jpg" alt="Example of X &amp; Y-axis mode"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/greebles1_axis_z.jpg" alt="Example of Z-axis mode"></td>
	</tr>
	<tr>
		<th>X &amp; Y-axis mode</th>
		<th>Z-axis mode</th>
	</tr>
</table>
<!-- END -->

## Count

<!-- SAMPLE greebles1_count 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/greebles1_count16.jpg" alt="Example of a 'Count' value of 16"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/greebles1_count32.jpg" alt="Example of a 'Count' value of 32"></td>
	</tr>
	<tr>
		<th>Count: <code>16</code></th>
		<th>Count: <code>32</code></th>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/greebles1_count64.jpg" alt="Example of a 'Count' value of 64"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/greebles1_count128.jpg" alt="Example of a 'Count' value of 128"></td>
	</tr>
	<tr>
		<th>Count: <code>64</code></th>
		<th>Count: <code>128</code></th>
	</tr>
</table>
<!-- END -->

## Width, Height & Depth

<!-- SAMPLE greebles1_variations 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/greebles1_depth1.jpg" alt="Example of a 'Depth' value of 1"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/greebles1_depth32.jpg" alt="Example of a 'Depth' value of 32"></td>
	</tr>
	<tr>
		<th>Depth: <code>1</code></th>
		<th>Depth: <code>32</code></th>
	</tr>
	<tr>
		<td valign="top"></td>
		<td valign="top"></td>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/greebles1_1x1x60.jpg" alt=""></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/greebles1_256x1x1.jpg" alt=""></td>
	</tr>
	<tr>
		<th></th>
		<th></th>
	</tr>
	<tr>
		<td valign="top">1x1x60</td>
		<td valign="top">256x1x1</td>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/greebles1_8x8x18.jpg" alt=""></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/greebles1_2x64x24.jpg" alt=""></td>
	</tr>
	<tr>
		<th></th>
		<th></th>
	</tr>
	<tr>
		<td valign="top">8x8x18</td>
		<td valign="top">2x64x24</td>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/greebles1_mode1_1x1x78.jpg" alt=""></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/greebles1_mode1_45x1x1.jpg" alt=""></td>
	</tr>
	<tr>
		<th></th>
		<th></th>
	</tr>
	<tr>
		<td valign="top">1x1x78</td>
		<td valign="top">45x1x1</td>
	</tr>
</table>
<!-- END -->

## Examples

<!-- SAMPLE greebles1_examples 1 -->
<table>
	<tr>
		<td width="100%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.6/greebles1_example0.jpg" alt="Example"></td>
	</tr>
	<tr>
		<th>Borg Cube</th>
	</tr>
</table>
<!-- END -->
