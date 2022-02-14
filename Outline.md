> The **`outline`** and **`outline2`** shaders replaces all voxels which match the selected colors, that are adjacent to another voxel of a different color, with a chosen color.
>
> `outline` and `outline2` are similar, except `outline2`  produces thinner lines.

<!-- TOC -->
- [Parameters](#parameters)
- [Examples](#examples)

## Parameters

Parameter | Description
--------- | -----------
**Color** | Color index for the outline (`0` will remove voxels)

## Examples

<!-- SAMPLE outline examples 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/outline_base.png" alt=""></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/outline.png" alt=""></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/outline2.png" alt=""></td>
	</tr>
	<tr>
		<td valign="top">Original</td>
		<td valign="top"><code>outline</code>, with the lighter green and white selected in the palette.</td>
		<td valign="top"><code>outline2</code>, with the lighter green and white selected in the palette.</td>
	</tr>
</table>
<!-- END -->
