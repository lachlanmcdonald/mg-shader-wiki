> The **gradient_radial** **[brush](Brush-Shaders)** which generates different styles of gradients from the colors selected from the palette in a radial (circular) pattern.
>
> To generate linear gradients, see the [**Gradient**](Gradient-Brush) brush.

<!-- TOC -->
- [Parameters](#parameters)
- [Mode](#mode)
- [Direction](#direction)
- [Flip](#flip)
- [Scale](#scale)
- [Power](#power)
- [Dither](#dither)

## Parameters

Parameter | Description
--------- | -----------
**Mode**       | Gradient mode (see below)
**Direction**  | Direction of the gradient (see below)
**Flip**       | Used to flip the direction of noise on the X/Y axis
**X Position** | Center of the radial on the X-axis (relative to the selected **Direction**)
**Y Position** | Center of the radial on the Y-axis (relative to the selected **Direction**)
**Scale**      | Scale of the gradient
**Power**      | Power of the gradient. Lower values produce longer gradients (less contrast), and higher values produce shaper and shorter gradients (more contrast).
**Dither**     | Amount of dithering between each of the selected colors
**Seed**       | Global seed (not all modes are affected)

## Mode

<!-- SAMPLE gradient_radial mode 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/gradient_radial_mode0.png" alt="Example of a 'Mode' value of 0"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/gradient_radial_mode1.png" alt="Example of a 'Mode' value of 1"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/gradient_radial_mode2.png" alt="Example of a 'Mode' value of 2"></td>
	</tr>
	<tr>
		<th>Mode: <code>0</code></th>
		<th>Mode: <code>1</code></th>
		<th>Mode: <code>2</code></th>
	</tr>
	<tr>
		<td valign="top">Interweaved noise</td>
		<td valign="top">Random noise</td>
		<td valign="top">Randomised scanlines</td>
	</tr>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/gradient_radial_mode3.png" alt="Example of a 'Mode' value of 3"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/gradient_radial_mode4.png" alt="Example of a 'Mode' value of 4"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/gradient_radial_mode5.png" alt="Example of a 'Mode' value of 5"></td>
	</tr>
	<tr>
		<th>Mode: <code>3</code></th>
		<th>Mode: <code>4</code></th>
		<th>Mode: <code>5</code></th>
	</tr>
	<tr>
		<td valign="top">Even scanlines</td>
		<td valign="top">Waveform noise</td>
		<td valign="top">Ordered Dithering (using a 4x4 Bayer Matrix)</td>
	</tr>
</table>
<!-- END -->

## Direction

<!-- SAMPLE gradient_radial direction 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/gradient_radial_direction0.png" alt="Example of a 'Direction' value of 0"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/gradient_radial_direction1.png" alt="Example of a 'Direction' value of 1"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/gradient_radial_direction2.png" alt="Example of a 'Direction' value of 2"></td>
	</tr>
	<tr>
		<th>Direction: <code>0</code></th>
		<th>Direction: <code>1</code></th>
		<th>Direction: <code>2</code></th>
	</tr>
</table>
<!-- END -->

## Flip

<!-- SAMPLE gradient_radial flip 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/gradient_radial_flip0.png" alt="Example of a 'Flip' value of 0"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/gradient_radial_flip1.png" alt="Example of a 'Flip' value of 1"></td>
	</tr>
	<tr>
		<th>Flip: <code>0</code></th>
		<th>Flip: <code>1</code></th>
	</tr>
</table>
<!-- END -->

## Scale

<!-- SAMPLE gradient_radial scale 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/gradient_radial_scale150.png" alt="Example of a 'Scale' value of 150"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/gradient_radial_scale200.png" alt="Example of a 'Scale' value of 200"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/gradient_radial_scale300.png" alt="Example of a 'Scale' value of 300"></td>
	</tr>
	<tr>
		<th>Scale: <code>150</code></th>
		<th>Scale: <code>200</code></th>
		<th>Scale: <code>300</code></th>
	</tr>
</table>
<!-- END -->

## Power

<!-- SAMPLE gradient_radial power 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/gradient_radial_power050.png" alt="Example of a 'Power' value of 0.5"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/gradient_radial_power100.png" alt="Example of a 'Power' value of 1.0"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/gradient_radial_power200.png" alt="Example of a 'Power' value of 2.0"></td>
	</tr>
	<tr>
		<th>Power: <code>0.5</code></th>
		<th>Power: <code>1.0</code></th>
		<th>Power: <code>2.0</code></th>
	</tr>
</table>
<!-- END -->

## Dither

<!-- SAMPLE gradient_radial dither 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/gradient_radial_dither0.png" alt="Example of a 'Dither' value of 0"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/gradient_radial_dither20.png" alt="Example of a 'Dither' value of 20"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/gradient_radial_dither40.png" alt="Example of a 'Dither' value of 40"></td>
	</tr>
	<tr>
		<th>Dither: <code>0</code></th>
		<th>Dither: <code>20</code></th>
		<th>Dither: <code>40</code></th>
	</tr>
</table>
<!-- END -->
