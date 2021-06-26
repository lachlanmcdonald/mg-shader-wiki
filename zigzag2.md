> **zigzag2** is a **[Zigzag brush](Zigzag-Brushes)** that generates zigzag patterns between two colors.

<!-- TOC -->
- [Arguments](#arguments)
- [Direction](#direction)
- [Examples](#examples)

## Arguments

Argument | Description
--------- | -----------
**Direction** | Direction of the pattern (see below)
**Width A** | Width of the primary lines
**Width B** | Width of the secondary lines
**Color A** | Color index of the primary line
**Color B** | Color index of the secondary line

Setting either of the colors to `0` will result in empty voxels.

## Direction

<!-- SAMPLE zigzag2_directions 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.4/zigzag2_direction0.png" alt="Example of a 'Direction' value of 0"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.4/zigzag2_direction1.png" alt="Example of a 'Direction' value of 1"></td>
	</tr>
	<tr>
		<th>Direction: <code>0</code></th>
		<th>Direction: <code>1</code></th>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.4/zigzag2_direction2.png" alt="Example of a 'Direction' value of 2"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.4/zigzag2_direction3.png" alt="Example of a 'Direction' value of 3"></td>
	</tr>
	<tr>
		<th>Direction: <code>2</code></th>
		<th>Direction: <code>3</code></th>
	</tr>
</table>
<!-- END -->

## Examples

<!-- SAMPLE zigzag2_examples 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.2/zigzag2_example0.png" alt=""></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.2/zigzag2_example1.png" alt=""></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.2/zigzag2_example2.png" alt=""></td>
	</tr>
</table>
<!-- END -->
