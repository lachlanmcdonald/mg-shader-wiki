> - The **soil**, **soil_replace** shaders adds a layer of voxels of a chosen color on top of voxels matching your selected color.
> - The **cover** shader adds a layer of voxels of a chosen color on top of all voxels in the volume.

## Arguments

Voxels are added on top of voxels matching the selected color.

Argument | Description
--------- | -----------
**Color** | Color index
**Headroom** | The number of voxels of space that must be available above the surface voxel. Setting to a higher value will stop voxels from forming in gaps

## Examples

<!-- SAMPLE soil_examples 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/cover_example0.jpg" alt="Example"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/cover_example1.jpg" alt="Example"></td>
	</tr>
	<tr>
		<td valign="top">Input volume</td>
		<td valign="top">Using <code>cover</code> to create the effect of a layer of snow</td>
	</tr>
</table>
<!-- END -->
