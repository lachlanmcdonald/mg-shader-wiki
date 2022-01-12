> **cellular3D** is a **[noise brush](Noise-Brushes)** that generates three-dimensional cellular noise (also known as [Worley noise](https://en.wikipedia.org/wiki/Worley_noise)).

<!-- TOC -->
- [Parameters](#parameters)
  - [Mode](#mode)
  - [Scale](#scale)
  - [Jitter](#jitter)
  - [Noise](#noise)
  - [Power](#power)
  - [Cavity](#cavity)

## Parameters

Parameter | Description
--------- | -----------
**Mode**   | See below
**Scale**  | Scale of the pattern
**Jitter** | Jitter of the points; values closer to `-100` and `100` are random, and values closer to `0` produce a more uniform pattern.
**Noise**  | Amount of additional noise to introduce to the pattern
**Power**  | Applies a power curve to the noise, values less than `1` reduce the curve, creating sharp peaks. Values greater than `1` round the curve, creating increasingly more rounded peaks.
**Cavity**  | Adjusts the spread of the inner cavity (for modes `0` and `3`)
**Seed**   | Global seed
**Tile X** | Tile offet on the X-axis
**Tile Y** | Tile offet on the Y-axis
**Tile z** | Tile offet on the Z-axis

**Tile X**, **Tile Y**, and **Tile Z** parameters are used to generate noise over multiple adjacent volumes. For instance, to create a terrain that exceeds the 256<sup>2</sup> size limit.

### Mode

<!-- SAMPLE cellular3D mode 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular3D_mode0_compressed.jpg" alt="Example of a 'Mode' value of 0"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular3D_mode1_compressed.jpg" alt="Example of a 'Mode' value of 1"></td>
	</tr>
	<tr>
		<th>Mode: <code>0</code></th>
		<th>Mode: <code>1</code></th>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular3D_mode2_compressed.jpg" alt="Example of a 'Mode' value of 2"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular3D_mode3_compressed.jpg" alt="Example of a 'Mode' value of 3"></td>
	</tr>
	<tr>
		<th>Mode: <code>2</code></th>
		<th>Mode: <code>3</code></th>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular3D_mode4_compressed.jpg" alt="Example of a 'Mode' value of 4"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular3D_mode5_compressed.jpg" alt="Example of a 'Mode' value of 5"></td>
	</tr>
	<tr>
		<th>Mode: <code>4</code></th>
		<th>Mode: <code>5</code></th>
	</tr>
</table>
<!-- END -->

### Scale

<!-- SAMPLE cellular3D scale 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular3D_scale10_compressed.jpg" alt="Example of a 'Scale' value of 10"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular3D_scale20_compressed.jpg" alt="Example of a 'Scale' value of 20"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular3D_scale40_compressed.jpg" alt="Example of a 'Scale' value of 40"></td>
	</tr>
	<tr>
		<th>Scale: <code>10</code></th>
		<th>Scale: <code>20</code></th>
		<th>Scale: <code>40</code></th>
	</tr>
</table>
<!-- END -->

### Jitter

<!-- SAMPLE cellular3D jitter 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular3D_jitter-100_compressed.jpg" alt="Example of a 'Jitter' value of -100"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular3D_jitter0_compressed.jpg" alt="Example of a 'Jitter' value of 0"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular3D_jitter100_compressed.jpg" alt="Example of a 'Jitter' value of 100"></td>
	</tr>
	<tr>
		<th>Jitter: <code>-100</code></th>
		<th>Jitter: <code>0</code></th>
		<th>Jitter: <code>100</code></th>
	</tr>
</table>
<!-- END -->

### Noise

<!-- SAMPLE cellular3D noise 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular3D_noise0_compressed.jpg" alt="Example of a 'Noise' value of 0"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular3D_noise25_compressed.jpg" alt="Example of a 'Noise' value of 25"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular3D_noise50_compressed.jpg" alt="Example of a 'Noise' value of 50"></td>
	</tr>
	<tr>
		<th>Noise: <code>0</code></th>
		<th>Noise: <code>25</code></th>
		<th>Noise: <code>50</code></th>
	</tr>
</table>
<!-- END -->

### Power

<!-- SAMPLE cellular3D power 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular3D_power050_compressed.jpg" alt="Example of a 'Power' value of 0.50"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular3D_power100_compressed.jpg" alt="Example of a 'Power' value of 1.00"></td>
	</tr>
	<tr>
		<th>Power: <code>0.50</code></th>
		<th>Power: <code>1.00</code></th>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular3D_power150_compressed.jpg" alt="Example of a 'Power' value of 1.50"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular3D_power200_compressed.jpg" alt="Example of a 'Power' value of 2.00"></td>
	</tr>
	<tr>
		<th>Power: <code>1.50</code></th>
		<th>Power: <code>2.00</code></th>
	</tr>
</table>
<!-- END -->

### Cavity

<!-- SAMPLE cellular3D cavity 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular3D_cavity20_compressed.jpg" alt="Example of a 'Cavity' value of 20"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular3D_cavity40_compressed.jpg" alt="Example of a 'Cavity' value of 400"></td>
	</tr>
	<tr>
		<th>Cavity: <code>20</code></th>
		<th>Cavity: <code>400</code></th>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular3D_cavity60_compressed.jpg" alt="Example of a 'Cavity' value of 60"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/cellular3D_cavity80_compressed.jpg" alt="Example of a 'Cavity' value of 80"></td>
	</tr>
	<tr>
		<th>Cavity: <code>60</code></th>
		<th>Cavity: <code>80</code></th>
	</tr>
</table>
<!-- END -->
