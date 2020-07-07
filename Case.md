> **case** surrounds/encases the voxels which match your selected color with a chosen color. This shader is similar to the _Dilation_ tool; except you can select an axis mode and target color.

<!-- TOC -->
- [Arguments](#arguments)
- [Axis Modes](#axis-modes)
- [Examples](#examples)

## Arguments

Argument | Description
--------- | -----------
**Color** | Color index

## Axis Modes

Axis modes can use used to only add voxels on certain axes.

<!-- SAMPLE case_axis 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/case_xyz.png" alt="Example of no set axis mode"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/case_x.png" alt="Example of X-axis mode"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/case_xy.png" alt="Example of X &amp; Y-axis mode"></td>
	</tr>
	<tr>
		<th>No set axis mode</th>
		<th>X-axis mode</th>
		<th>X &amp; Y-axis mode</th>
	</tr>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/case_y.png" alt="Example of Y-axis mode"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/case_z.png" alt="Example of Z-axis mode"></td>
	</tr>
	<tr>
		<th>Y-axis mode</th>
		<th>Z-axis mode</th>
	</tr>
</table>
<!-- END -->

## Examples

<!-- SAMPLE case_examples 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/case_example0.jpg" alt="Example"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/case_example1.jpg" alt="Example"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.5/case_example2.jpg" alt="Example"></td>
	</tr>
	<tr>
		<td valign="top">Original</td>
		<td valign="top">Using <code>case</code> and cloud materials to create eerie glows</td>
		<td valign="top">Using <code>case</code> and SSR materials to create a plastic/rubber texture</td>
	</tr>
</table>
<!-- END -->

