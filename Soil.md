> The **`soil`**, **`soil_replace`** shaders adds a layer of voxels of a color on top of voxels matching the selected colors. `soil` adds the voxels on top, and `soil_replace` replaces the voxels.
> 
> This shader is similar to the [`cover`](Cover) shader, except `cover` adds a layer to all voxels, where these shaders only works on the selected colors.

## Parameters

Parameter | Description
--------- | -----------
**Color** | Color index
**Headroom** | The number of voxels of space that must be available above the surface voxel. Setting to a higher value will stop voxels from forming in gaps

## Headroom

<!-- SAMPLE soil headroom 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/soil_headroom_1.png" alt=""></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/soil_headroom_10.png" alt=""></td>
	</tr>
	<tr>
		<td valign="top">A <strong>Headroom</strong> of <code>1</code> checks that 1 voxel higher to make sure there is room.</td>
		<td valign="top">A <strong>Headroom</strong> of <code>10</code> checks that 10 voxels higher to make sure there is room. Resulting in gaps where there is overhang from other voxels.</td>
	</tr>
</table>
<!-- END -->
