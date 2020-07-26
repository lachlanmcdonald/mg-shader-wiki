> **stairs** is a **[stairs brush](Stairs-Brushes)** that generates stairs which extend from the base of the brush.

<!-- TOC -->
- [Parameters](#parameters)
- [Mode](#mode)
- [Direction](#direction)
- [Height](#height)

## Parameters

Parameter | Description
--------- | -----------
**Mode** | Automate one of the parameters (see below)
**Direction** | The facing direction of the stairs
**Count** | The number of runs to fit within the brushes dimensions. If the box's dimensions are not divisible by the count, the depth of each run will be inconsistent
**Height** | The height of each run

## Mode

Mode | Description
---- | -----------
`0` |  All parameters are used as-is
`1` |  The **Height** of each run is adjusted to fill the available space (the value of the parameter is ignored). **Count** can still be adjusted
`2` | **Count** is adjusted to fill the available space (the value of the parameter is ignored). **Height** can still be adjusted

## Direction

<!-- SAMPLE stairs_directions 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/stairs_direction0.png" alt="Example of a direction of 0"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/stairs_direction1.png" alt="Example of a direction of 1"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/stairs_direction2.png" alt="Example of a direction of 2"></td>
	</tr>
	<tr>
		<th>Direction: <code>0</code></th>
		<th>Direction: <code>1</code></th>
		<th>Direction: <code>2</code></th>
	</tr>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/stairs_direction3.png" alt="Example of a direction of 3"></td>
	</tr>
	<tr>
		<th>Direction: <code>3</code></th>
	</tr>
</table>
<!-- END -->

## Height

<!-- SAMPLE stairs_height 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/stairs_height1.png" alt="Example of a height of 1"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/stairs_height2.png" alt="Example of a height of 2"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/stairs_height3.png" alt="Example of a height of 3"></td>
	</tr>
	<tr>
		<th>Height: <code>1</code></th>
		<th>Height: <code>2</code></th>
		<th>Height: <code>3</code></th>
	</tr>
</table>
<!-- END -->
