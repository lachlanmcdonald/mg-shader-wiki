> **`stairs_runs`** is a **[stairs brush](Stairs-Brushes)** that generates only stair runs; with additional options for the size and spacing of the runs.

<!-- TOC -->
- [Parameters](#parameters)
  - [Mode](#mode)
  - [Count](#count)
  - [Height](#height)
  - [X/Y Gap](#xy-gap)
  - [Z Gap](#z-gap)

## Parameters

Parameter | Description
--------- | -----------
**Mode**      | Automate one of the parameters (see below)
**Direction** | The facing direction of the stairs
**Count**     | The number of runs to fit within the brushes dimensions. If the box's dimensions are not divisible by the count, the depth of each run will be inconsistent
**Height**    | The height of each run
**X/Y Gap**   | The distance between each run of adjacent stairs
**Z Gap**     | The distance between each run and the next run above it (also known as the _rise._)

### Mode

Mode | Description
---- | -----------
`0` | All parameters are used as-is
`1` | The **Height** of each run is adjusted to fill the available space (the value of the parameter is ignored). **Count** and **Z Gap** can still be adjusted
`2` | **Count** is adjusted to fill the available space (the value of the parameter is ignored). **Height** and **Z Gap** can still be adjusted
`3` | **Z Gap** is adjusted to fill the available space (the value of the parameter is ignored). **Count** and **Height** can still be adjusted

### Count

<!-- SAMPLE stairs_runs count 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/stairs_count_2.png" alt="Example of a 'Count' value of 2"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/stairs_count_4.png" alt="Example of a 'Count' value of 4"></td>
	</tr>
	<tr>
		<th>Count: <code>2</code></th>
		<th>Count: <code>4</code></th>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/stairs_count_6.png" alt="Example of a 'Count' value of 6"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/stairs_count_8.png" alt="Example of a 'Count' value of 8"></td>
	</tr>
	<tr>
		<th>Count: <code>6</code></th>
		<th>Count: <code>8</code></th>
	</tr>
</table>
<!-- END -->

### Height

<!-- SAMPLE stairs_runs height 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/stairs_height_1.png" alt="Example of a 'Height' value of 1"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/stairs_height_2.png" alt="Example of a 'Height' value of 2"></td>
	</tr>
	<tr>
		<th>Height: <code>1</code></th>
		<th>Height: <code>2</code></th>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/stairs_height_3.png" alt="Example of a 'Height' value of 3"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/stairs_height_4.png" alt="Example of a 'Height' value of 4"></td>
	</tr>
	<tr>
		<th>Height: <code>3</code></th>
		<th>Height: <code>4</code></th>
	</tr>
</table>
<!-- END -->

### X/Y Gap

<!-- SAMPLE stairs_runs xy_gap 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/stairs_xy_gap_0.png" alt="Example of a X/Y Gap of 0"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/stairs_xy_gap_1.png" alt="Example of a X/Y Gap of 1"></td>
	</tr>
	<tr>
		<th>X/Y Gap: <code>0</code></th>
		<th>X/Y Gap: <code>1</code></th>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/stairs_xy_gap_2.png" alt="Example of a X/Y Gap of 2"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/stairs_xy_gap_3.png" alt="Example of a X/Y Gap of 3"></td>
	</tr>
	<tr>
		<th>X/Y Gap: <code>2</code></th>
		<th>X/Y Gap: <code>3</code></th>
	</tr>
</table>
<!-- END -->

### Z Gap

<!-- SAMPLE stairs_runs z_gap 2 -->
<table>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/stairs_z_gap_0.png" alt="Example of a Z Gap of 0"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/stairs_z_gap_1.png" alt="Example of a Z Gap of 1"></td>
	</tr>
	<tr>
		<th>Z Gap: <code>0</code></th>
		<th>Z Gap: <code>1</code></th>
	</tr>
	<tr>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/stairs_z_gap_2.png" alt="Example of a Z Gap of 2"></td>
		<td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/stairs_z_gap_3.png" alt="Example of a Z Gap of 3"></td>
	</tr>
	<tr>
		<th>Z Gap: <code>2</code></th>
		<th>Z Gap: <code>3</code></th>
	</tr>
</table>
<!-- END -->
