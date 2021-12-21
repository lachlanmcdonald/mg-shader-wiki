> **cellular2D** is a **[noise brush](Noise-Brushes)** that generates two-dimensional cellular noise (also known as [Worley noise](https://en.wikipedia.org/wiki/Worley_noise)).

<!-- TOC -->
- [Parameters](#parameters)
- [Mode](#mode)
- [Scale](#scale)
- [Jitter](#jitter)
- [Noise](#noise)
- [Power](#power)
- [Steps](#steps)

## Parameters

Parameter | Description
--------- | -----------
**Mode**   | See below
**Scale**  | Scale of the pattern
**Jitter** | Jitter of the points; values closer to `-100` and `100` are random, and values closer to `0` produce a more uniform pattern.
**Noise**  | Amount of additional noise to introduce to the pattern
**Power**  | Applies a power curve to the noise, values less than `1` reduce the curve, creating sharp peaks. Values greater than `1` round the curve, creating increasingly more rounded peaks.
**Steps**  | For values greater than `0`, limit the noise to evenly spaced steps.
**Seed**   | Global seed
**Tile X** | Tile offet on the X-axis
**Tile Y** | Tile offet on the Y-axis

**Tile X** and **Tile Y** parameters are used to generate noise over multiple adjacent volumes. For instance, to create a terrain that exceeds the 256<sup>2</sup> size limit.

## Mode

<!-- SAMPLE cellular2D_mode 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular2D_mode0_compressed.jpg" alt="Example of a 'Mode' value of 0"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular2D_mode1_compressed.jpg" alt="Example of a 'Mode' value of 1"></td>
	</tr>
	<tr>
		<th>Mode: <code>0</code></th>
		<th>Mode: <code>1</code></th>
	</tr>
	<tr>
		<td valign="top">Generate mounds and peaks</td>
		<td valign="top">Generate dips</td>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular2D_mode2_compressed.jpg" alt="Example of a 'Mode' value of 2"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular2D_mode3_compressed.jpg" alt="Example of a 'Mode' value of 3"></td>
	</tr>
	<tr>
		<th>Mode: <code>2</code></th>
		<th>Mode: <code>3</code></th>
	</tr>
	<tr>
		<td valign="top">Generate mounds and peaks (using the second closest point)</td>
		<td valign="top">Generate dips (using the second closest point)</td>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular2D_mode4_compressed.jpg" alt="Example of a 'Mode' value of 4"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular2D_mode5_compressed.jpg" alt="Example of a 'Mode' value of 5"></td>
	</tr>
	<tr>
		<th>Mode: <code>4</code></th>
		<th>Mode: <code>5</code></th>
	</tr>
	<tr>
		<td valign="top">Generates the noise pattern and ignores the Z-axis</td>
		<td valign="top">Generates the noise pattern and ignores the Z-axis (using the second closest point)</td>
	</tr>
</table>
<!-- END -->

## Scale

<!-- SAMPLE cellular2D_scale 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular2D_scale20_compressed.jpg" alt="Example of a 'Scale' value of 20"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular2D_scale40_compressed.jpg" alt="Example of a 'Scale' value of 40"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular2D_scale80_compressed.jpg" alt="Example of a 'Scale' value of 80"></td>
	</tr>
	<tr>
		<th>Scale: <code>20</code></th>
		<th>Scale: <code>40</code></th>
		<th>Scale: <code>80</code></th>
	</tr>
</table>
<!-- END -->

## Jitter

<!-- SAMPLE cellular2D_jitter 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular2D_jitter-100_compressed.jpg" alt="Example of a 'Jitter' value of -100"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular2D_jitter0_compressed.jpg" alt="Example of a 'Jitter' value of 0"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular2D_jitter100_compressed.jpg" alt="Example of a 'Jitter' value of 100"></td>
	</tr>
	<tr>
		<th>Jitter: <code>-100</code></th>
		<th>Jitter: <code>0</code></th>
		<th>Jitter: <code>100</code></th>
	</tr>
</table>
<!-- END -->

## Noise

<!-- SAMPLE cellular2D_noise 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular2D_noise0_compressed.jpg" alt="Example of a 'Noise' value of 0"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular2D_noise25_compressed.jpg" alt="Example of a 'Noise' value of 25"></td>
	</tr>
	<tr>
		<th>Noise: <code>0</code></th>
		<th>Noise: <code>25</code></th>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular2D_noise50_compressed.jpg" alt="Example of a 'Noise' value of 50"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular2D_noise75_compressed.jpg" alt="Example of a 'Noise' value of 75"></td>
	</tr>
	<tr>
		<th>Noise: <code>50</code></th>
		<th>Noise: <code>75</code></th>
	</tr>
</table>
<!-- END -->

## Power

<!-- SAMPLE cellular2D_power 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular2D_power050_compressed.jpg" alt="Example of a 'Power' value of 0.50"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular2D_power100_compressed.jpg" alt="Example of a 'Power' value of 1.00"></td>
	</tr>
	<tr>
		<th>Power: <code>0.50</code></th>
		<th>Power: <code>1.00</code></th>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular2D_power150_compressed.jpg" alt="Example of a 'Power' value of 1.50"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular2D_power200_compressed.jpg" alt="Example of a 'Power' value of 2.00"></td>
	</tr>
	<tr>
		<th>Power: <code>1.50</code></th>
		<th>Power: <code>2.00</code></th>
	</tr>
</table>
<!-- END -->

## Steps

<!-- SAMPLE cellular2D_steps 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular2D_steps0_compressed.jpg" alt="Example of a 'Steps' value of 0"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular2D_steps8_compressed.jpg" alt="Example of a 'Steps' value of 8"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular2D_steps16_compressed.jpg" alt="Example of a 'Steps' value of 16"></td>
	</tr>
	<tr>
		<th>Steps: <code>0</code></th>
		<th>Steps: <code>8</code></th>
		<th>Steps: <code>16</code></th>
	</tr>
</table>
<!-- END -->
