> The **grass_fit** shader generates random columns of voxels with a constant distribution; similar to grass or small plants. The color of the voxels is determined by the selected colors in the palette.
>
> This shader is similar to the [Grass brush shader](Grass-Brush), except this shader is applied to the entire volume.

<!-- TOC -->
- [Parameters](#parameters)
- [Examples](#examples)
- [Notes](#notes)

## Parameters

> See [Grass brush shader](Grass-Brush).

Parameter | Description
--------- | -----------
**Mode** | Color mode
**Density** | Size of the area in which a line should be generated. Increasing density will increase the spacing between lines
**Height** | Maximum height of each column
**Seed** | Global seed

## Examples

<!-- SAMPLE grass_fit examples 1 -->
<table>
	<tr>
		<td width="100%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/grass_fit0.jpg" alt="Before"></td>
	</tr>
	<tr>
		<td width="100%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.13.0/grass_fit1.jpg" alt="After"></td>
	</tr>
</table>
<!-- END -->

## Notes

- The shader will cause issues when used with the _Marquee Select_ tool
