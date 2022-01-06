> **gradient** is a **[brush](Brush-Shaders)** which generates different styles of gradients from the selected colors.

<!-- TOC -->
- [Parameters](#parameters)
- [Mode](#mode)
- [Direction](#direction)
- [Noise](#noise)

## Parameters

Parameter | Description
--------- | -----------
**Mode**      | Gradient mode (see below)
**Direction** | Direction of the gradient (see below)
**Noise**     | Amount of noise to introduce between each of the selected.
**Seed**      | Global seed (not all modes are affected)

## Mode

<!-- SAMPLE gradient mode 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/gradient_mode0_compressed.jpg" alt="Example of a 'Mode' value of 0"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/gradient_mode1_compressed.jpg" alt="Example of a 'Mode' value of 1"></td>
	</tr>
	<tr>
		<th>Mode: <code>0</code></th>
		<th>Mode: <code>1</code></th>
	</tr>
	<tr>
		<td valign="top">Interweaved noise</td>
		<td valign="top">Random noise</td>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/gradient_mode2_compressed.jpg" alt="Example of a 'Mode' value of 2"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/gradient_mode3_compressed.jpg" alt="Example of a 'Mode' value of 3"></td>
	</tr>
	<tr>
		<th>Mode: <code>2</code></th>
		<th>Mode: <code>3</code></th>
	</tr>
	<tr>
		<td valign="top">Randomised scanlines</td>
		<td valign="top">Even scanlines</td>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/gradient_mode4_compressed.jpg" alt="Example of a 'Mode' value of 4"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/gradient_mode5_compressed.jpg" alt="Example of a 'Mode' value of 5"></td>
	</tr>
	<tr>
		<th>Mode: <code>4</code></th>
		<th>Mode: <code>5</code></th>
	</tr>
	<tr>
		<td valign="top">Waveform noise</td>
		<td valign="top">Ordered Dithering (using a 4x4 Bayer Matrix)</td>
	</tr>
</table>
<!-- END -->

## Direction

<!-- SAMPLE gradient direction 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/gradient_direction0_compressed.jpg" alt="Example of a 'Direction' value of 0"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/gradient_direction1_compressed.jpg" alt="Example of a 'Direction' value of 1"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/gradient_direction2_compressed.jpg" alt="Example of a 'Direction' value of 2"></td>
	</tr>
	<tr>
		<th>Direction: <code>0</code></th>
		<th>Direction: <code>1</code></th>
		<th>Direction: <code>2</code></th>
	</tr>
	<tr>
		<td valign="top">Gradient across the Z-axis</td>
		<td valign="top">Gradient across the Z-axis (in reverse)</td>
		<td valign="top">Gradient across the Y-axis</td>
	</tr>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/gradient_direction3_compressed.jpg" alt="Example of a 'Direction' value of 3"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/gradient_direction4_compressed.jpg" alt="Example of a 'Direction' value of 4"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/gradient_direction5_compressed.jpg" alt="Example of a 'Direction' value of 5"></td>
	</tr>
	<tr>
		<th>Direction: <code>3</code></th>
		<th>Direction: <code>4</code></th>
		<th>Direction: <code>5</code></th>
	</tr>
	<tr>
		<td valign="top">Gradient across the Y-axis (in reverse)</td>
		<td valign="top">Gradient across the X-axis</td>
		<td valign="top">Gradient across the X-axis (in reverse)</td>
	</tr>
</table>
<!-- END -->

## Noise

<!-- SAMPLE gradient noise 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/gradient_noise00_compressed.jpg" alt="Example of a 'Noise' value of 0"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/gradient_noise05_compressed.jpg" alt="Example of a 'Noise' value of 5"></td>
	</tr>
	<tr>
		<th>Noise: <code>0</code></th>
		<th>Noise: <code>5</code></th>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/gradient_noise20_compressed.jpg" alt="Example of a 'Noise' value of 20"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/gradient_noise40_compressed.jpg" alt="Example of a 'Noise' value of 40"></td>
	</tr>
	<tr>
		<th>Noise: <code>20</code></th>
		<th>Noise: <code>40</code></th>
	</tr>
</table>
<!-- END -->
