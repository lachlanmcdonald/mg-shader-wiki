> The **`cover`** shader adds a layer of voxels of the selected colors on top of all voxels in the volume.
>
> This shader is similar to the [`soil`](Soil) shader, except `cover` adds a layer to all voxels, where `soil` only works on the selected colors.

## Parameters

Parameter | Description
--------- | -----------
**Headroom** | The number of voxels of space that must be available above the surface voxel. Setting to a higher value will stop voxels from forming in gaps
**Noise** | Chance that a voxel will not be added. When `0`, no voxels are skipped. Values closer to `100` will cause voxels to be skipped at random.
**Seed** | Global seed

<!-- SAMPLE cover variations 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/cover.png" alt=""></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/cover_1.png" alt=""></td>
	</tr>
	<tr>
		<td valign="top">Original</td>
		<td valign="top"><code>cover</code> with a single selected color</td>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/cover_4.png" alt=""></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/cover_noise_50.png" alt=""></td>
	</tr>
	<tr>
		<td valign="top"><code>cover</code> with multiple selected colors</td>
		<td valign="top"><code>cover</code> with multiple selected colors and a <code>noise</code> value of <code>0.5</code></td>
	</tr>
</table>
<!-- END -->

## Examples

<!-- SAMPLE cover examples 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/cover_example0.jpg" alt=""></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/cover_example1.jpg" alt=""></td>
	</tr>
	<tr>
		<td valign="top">Original</td>
		<td valign="top">Using <code>cover</code> to create the effect of a layer of snow</td>
	</tr>
</table>
<!-- END -->
