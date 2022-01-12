> The **terrain** [brush](Brush-Shaders) generates a terrain-like topography by combining different types of noise and [Fractional Brownian motion](https://en.wikipedia.org/wiki/Fractional_Brownian_motion).

<!-- TOC -->
- [Parameters](#parameters)
  - [Mode](#mode)
  - [Scale](#scale)
  - [Iterations](#iterations)
  - [Octaves](#octaves)
  - [Contrast](#contrast)
  - [Shift](#shift)
  - [Gain](#gain)
  - [Lucanarity](#lucanarity)
  - [Noise](#noise)

## Parameters

Parameter | Description
--------- | -----------
**Mode**       | Color mode (see below)
**Direction**  | Direction. A value of `1` inverts the terrain.
**Scale**      | Scale of the terrain
**Iterations** | Number of iterations, lower values produce less terrain features and high values more features. This can be roughly thought of as increasing the height-map resolution.
**Octaves**    | Number of octives when for generating displacements of the terrain (small features). Higher values produce more features (but more noise) and lower values produce less features (and smoother terrain).
**Contrast**   | Adjusts the contrast of the height-map. The default value of `50` represents the mid-point, valueas towards `100` increase the depth of high and low values. Where as values towards `0` produces smoother terrain. For low number of *Iterations* or *Octaves*, it might be necessary to increase the contrast.
**Shift**      | Shift the mid-point of the height-map. The default value of `50` represents the normal mid-point.
**Gain**       | Influence of each iteration. Effectively this multiplies each iteration.Smaller values produce smoother terrain, and higher values produce more turbulance and noise.
**Lacunarity** | Lacunarity
**Noise**      | Additional color noise (does not change the terrain.)
**Tile X** | Tile offet on the X-axis
**Tile Y** | Tile offet on the Y-axis

**Tile X** and **Tile Y** parameters are used to generate noise over multiple adjacent volumes. For instance, to create a terrain that exceeds the 256<sup>2</sup> size limit.

### Mode

<!-- SAMPLE terrain mode 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/terrain_mode0.jpg" alt="Example of a 'Mode' value of 0"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/terrain_mode1.jpg" alt="Example of a 'Mode' value of 1"></td>
	</tr>
	<tr>
		<th>Mode: <code>0</code></th>
		<th>Mode: <code>1</code></th>
	</tr>
</table>
<!-- END -->

### Scale

<!-- SAMPLE terrain scale 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/terrain_scale25.jpg" alt="Example of a 'Scale' value of 25"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/terrain_scale50.jpg" alt="Example of a 'Scale' value of 50"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/terrain_scale75.jpg" alt="Example of a 'Scale' value of 75"></td>
	</tr>
	<tr>
		<th>Scale: <code>25</code></th>
		<th>Scale: <code>50</code></th>
		<th>Scale: <code>75</code></th>
	</tr>
</table>
<!-- END -->

### Iterations

<!-- SAMPLE terrain iterations 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/terrain_iterations1.jpg" alt="Example of a 'Iterations' value of 1"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/terrain_iterations2.jpg" alt="Example of a 'Iterations' value of 2"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/terrain_iterations3.jpg" alt="Example of a 'Iterations' value of 3"></td>
	</tr>
	<tr>
		<th>Iterations: <code>1</code></th>
		<th>Iterations: <code>2</code></th>
		<th>Iterations: <code>3</code></th>
	</tr>
</table>
<!-- END -->

### Octaves

<!-- SAMPLE terrain octaves 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/terrain_octaves1.jpg" alt="Example of a 'Octaves' value of 1"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/terrain_octaves2.jpg" alt="Example of a 'Octaves' value of 2"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/terrain_octaves3.jpg" alt="Example of a 'Octaves' value of 3"></td>
	</tr>
	<tr>
		<th>Octaves: <code>1</code></th>
		<th>Octaves: <code>2</code></th>
		<th>Octaves: <code>3</code></th>
	</tr>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/terrain_octaves4.jpg" alt="Example of a 'Octaves' value of 4"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/terrain_octaves5.jpg" alt="Example of a 'Octaves' value of 5"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/terrain_octaves6.jpg" alt="Example of a 'Octaves' value of 6"></td>
	</tr>
	<tr>
		<th>Octaves: <code>4</code></th>
		<th>Octaves: <code>5</code></th>
		<th>Octaves: <code>6</code></th>
	</tr>
</table>
<!-- END -->

### Contrast

<!-- SAMPLE terrain contrast 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/terrain_contrast30.jpg" alt="Example of a 'Contrast' value of 30"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/terrain_contrast50.jpg" alt="Example of a 'Contrast' value of 50"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/terrain_contrast70.jpg" alt="Example of a 'Contrast' value of 70"></td>
	</tr>
	<tr>
		<th>Contrast: <code>30</code></th>
		<th>Contrast: <code>50</code></th>
		<th>Contrast: <code>70</code></th>
	</tr>
</table>
<!-- END -->

### Shift

<!-- SAMPLE terrain shift 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/terrain_shift20.jpg" alt="Example of a 'Shift' value of 20"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/terrain_shift40.jpg" alt="Example of a 'Shift' value of 40"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/terrain_shift60.jpg" alt="Example of a 'Shift' value of 60"></td>
	</tr>
	<tr>
		<th>Shift: <code>20</code></th>
		<th>Shift: <code>40</code></th>
		<th>Shift: <code>60</code></th>
	</tr>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/terrain_shift80.jpg" alt="Example of a 'Shift' value of 80"></td>
	</tr>
	<tr>
		<th>Shift: <code>80</code></th>
	</tr>
</table>
<!-- END -->

### Gain

<!-- SAMPLE terrain gain 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/terrain_gain50.jpg" alt="Example of a 'Gain' value of 50"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/terrain_gain65.jpg" alt="Example of a 'Gain' value of 65"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/terrain_gain80.jpg" alt="Example of a 'Gain' value of 80"></td>
	</tr>
	<tr>
		<th>Gain: <code>50</code></th>
		<th>Gain: <code>65</code></th>
		<th>Gain: <code>80</code></th>
	</tr>
</table>
<!-- END -->

### Lucanarity

<!-- SAMPLE terrain lucanarity 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/terrain_lucanarity0.jpg" alt="Example of a 'Lucanarity' value of 0"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/terrain_lucanarity100.jpg" alt="Example of a 'Lucanarity' value of 100"></td>
	</tr>
	<tr>
		<th>Lucanarity: <code>0</code></th>
		<th>Lucanarity: <code>100</code></th>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/terrain_lucanarity200.jpg" alt="Example of a 'Lucanarity' value of 200"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/terrain_lucanarity300.jpg" alt="Example of a 'Lucanarity' value of 300"></td>
	</tr>
	<tr>
		<th>Lucanarity: <code>200</code></th>
		<th>Lucanarity: <code>300</code></th>
	</tr>
</table>
<!-- END -->

### Noise

<!-- SAMPLE terrain noise 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/terrain_noise0.jpg" alt="Example of a 'Noise' value of 0"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/terrain_noise50.jpg" alt="Example of a 'Noise' value of 50"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/terrain_noise100.jpg" alt="Example of a 'Noise' value of 100"></td>
	</tr>
	<tr>
		<th>Noise: <code>0</code></th>
		<th>Noise: <code>50</code></th>
		<th>Noise: <code>100</code></th>
	</tr>
</table>
<!-- END -->
