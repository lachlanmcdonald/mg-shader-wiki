> **stairs_stringer** is a **[stairs brush](Stairs-Brushes)** that generates stairs with a stringer of a specific height.

<!-- TOC -->
- [Parameters](#parameters)
- [Mode](#mode)
- [Direction](#direction)
- [Stringer](#stringer)

## Parameters

Parameter | Description
--------- | -----------
**Mode** | Automate one of the parameters (see below)
**Direction** | The facing direction of the stairs
**Count** | The number of runs to fit within the brushes dimensions. If the box's dimensions are not divisible by the count, the depth of each run will be inconsistent
**Height** | The height of each run
**Stringer** | The height of the stringer (the area extending beneath each run)

## Mode

Mode | Description
---- | -----------
`0` | All parameters are used as-is
`1` | The **Height** of each run is adjusted to fill the available space (the value of the parameter is ignored). **Count** and **Stringer** can still be adjusted
`2` | **Count** is adjusted to fill the available space (the value of the parameter is ignored). **Height** and **Stringer** can still be adjusted
`3` | **Stringer** is adjusted to fill the available space (the value of the parameter is ignored). **Count** and **Height** can still be adjusted

## Direction

<!-- SAMPLE stairs_stringer_directions 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/stairs_stringer_direction0.png" alt="Example of a direction of 0"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/stairs_stringer_direction1.png" alt="Example of a direction of 1"></td>
	</tr>
	<tr>
		<th>Direction: <code>0</code></th>
		<th>Direction: <code>1</code></th>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/stairs_stringer_direction2.png" alt="Example of a direction of 2"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/stairs_stringer_direction3.png" alt="Example of a direction of 3"></td>
	</tr>
	<tr>
		<th>Direction: <code>2</code></th>
		<th>Direction: <code>3</code></th>
	</tr>
</table>
<!-- END -->

## Stringer

<!-- SAMPLE stairs_stringer_stringers 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/stairs_stringer_stringer1.png" alt="Example of a Stringer of 1"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/stairs_stringer_stringer2.png" alt="Example of a Stringer of 2"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.3/stairs_stringer_stringer4.png" alt="Example of a Stringer of 3"></td>
	</tr>
	<tr>
		<th>Stringer: <code>1</code></th>
		<th>Stringer: <code>2</code></th>
		<th>Stringer: <code>4</code></th>
	</tr>
</table>
<!-- END -->

