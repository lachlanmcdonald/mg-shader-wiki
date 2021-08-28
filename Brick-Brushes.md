> The **Brick [brushes](Brush-Shaders)** generates alternating rows of randomly colored bricks. The colors of the bricks are determined by the selected colors in the palette.
> 
> There are two shaders, **`bricks`** and **`bricks_vert`**, that are functionally identical except bricks are offset horizontally for `bricks` and vertically for `bricks_vert`.

<!-- TOC -->
- [Parameters](#parameters)
- [Mode](#mode)
- [Grout Size](#grout-size)
- [Noise](#noise)
- [Threshold](#threshold)

## Parameters

Parameter | Description
--------- | -----------
**Mode** | Color mode (see below)
**Direction** | Facing direction of the bricks
**Width** | Width of the brick
**Height** | Height of each brick
**Depth** | Depth of each brick
**Grout Size** | Width of the grout between bricks, or `0` for no grout (see below)
**Grout Color** | Color index for the grout color, or `0` for gaps.
**Offset** | Misalignment of bricks per row (a value of `0` will determine the misalignment automatically)
**Noise** | Randomness of the colors within each brick. Values closer to `0` produce solid colored bricks, where as values closer to `1` produce noisy bricks (see below)
**Threshold** | Likelihood of a brick being placed. The default of `1.0` means all bricks are placed, and lower values will result in missing bricks (see below)

## Mode

<!-- SAMPLE brick_mode 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/brick_mode_0.png" alt="Example of a 'Mode' value of 0"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/brick_mode_1.png" alt="Example of a 'Mode' value of 1"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/brick_mode_2.png" alt="Example of a 'Mode' value of 2"></td>
	</tr>
	<tr>
		<th>Mode: <code>0</code></th>
		<th>Mode: <code>1</code></th>
		<th>Mode: <code>2</code></th>
	</tr>
	<tr>
		<td valign="top">Brick colors are chosen at random</td>
		<td valign="top">Brick are colored as a gradient of the selected colors along the z-axis</td>
		<td valign="top">Same as mode <code>1</code> but in reverse</td>
	</tr>
</table>
<!-- END -->

## Grout Size

<!-- SAMPLE brick_grout 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/brick_grout_0.png" alt="Example of a 'Grout' value of 0"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/brick_grout_1.png" alt="Example of a 'Grout' value of 1"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/brick_grout_2.png" alt="Example of a 'Grout' value of 2"></td>
	</tr>
	<tr>
		<th>Grout: <code>0</code></th>
		<th>Grout: <code>1</code></th>
		<th>Grout: <code>2</code></th>
	</tr>
</table>
<!-- END -->

## Noise

<!-- SAMPLE brick_noise 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/brick_noise_0.png" alt="Example of a 'noise' value of 0"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/brick_noise_25.png" alt="Example of a 'noise' value of 25"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/brick_noise_75.png" alt="Example of a 'noise' value of 75"></td>
	</tr>
	<tr>
		<th>noise: <code>0</code></th>
		<th>noise: <code>25</code></th>
		<th>noise: <code>75</code></th>
	</tr>
</table>
<!-- END -->

## Threshold

<!-- SAMPLE brick_threshold 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/brick_threshold_100.png" alt="Example of a 'Threshold' value of 100"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/brick_threshold_80.png" alt="Example of a 'Threshold' value of 80"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/brick_threshold_60.png" alt="Example of a 'Threshold' value of 60"></td>
	</tr>
	<tr>
		<th>Threshold: <code>100</code></th>
		<th>Threshold: <code>80</code></th>
		<th>Threshold: <code>60</code></th>
	</tr>
</table>
<!-- END -->
