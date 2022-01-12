> **zigzag3** is a **[Zigzag brush](Zigzag-Brushes)** that generates zigzag patterns between three colors.

<!-- TOC -->
- [Parameters](#parameters)
- [Direction](#direction)
- [Examples](#examples)

## Parameters

Parameter | Description
--------- | -----------
**Direction** | Direction of the pattern (see below)
**Width A** | Width of the primary lines
**Width B** | Width of the secondary lines
**Width C** | Width of the tertiary lines
**Color A** | Color index of the primary line
**Color B** | Color index of the secondary line
**Color C** | Color index of the tertiary line

Setting any of the colors to `0` will result in empty voxels.

> **Note:** Zigzag brushes have not yet been updated to use the new color selection system.

### Direction

<!-- SAMPLE zigzag3 directions 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.4/zigzag3_direction0.png" alt="Example of a 'Direction' value of 0"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.4/zigzag3_direction1.png" alt="Example of a 'Direction' value of 1"></td>
	</tr>
	<tr>
		<th>Direction: <code>0</code></th>
		<th>Direction: <code>1</code></th>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.4/zigzag3_direction2.png" alt="Example of a 'Direction' value of 2"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.4/zigzag3_direction3.png" alt="Example of a 'Direction' value of 3"></td>
	</tr>
	<tr>
		<th>Direction: <code>2</code></th>
		<th>Direction: <code>3</code></th>
	</tr>
</table>
<!-- END -->

## Examples

<!-- SAMPLE zigzag3 examples 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.2/zigzag3_example0.png" alt="Example"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.2/zigzag3_example1.png" alt="Example"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.2/zigzag3_example2.png" alt="Example"></td>
	</tr>
</table>
<!-- END -->
