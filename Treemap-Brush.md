> The **treemap** [brush](Brush-Shaders) generates a [treemap pattern](https://en.wikipedia.org/wiki/Treemapping) by randomly dividing the area until a limit on the number of iterations or size is reached.

<!-- TOC -->
- [Parameters](#parameters)
- [Mode](#mode)

## Parameters

Parameter | Description
--------- | -----------
**Mode**  | Color mode (see below)
**Direction**  | See below
**Iterations**  | Maximum number of iterations to perform. The number of iterations affects the size of the pattern, with smaller iterations producing larger clusters, and vice versa.
**Min Size**  | Attempt to enforce a minimum size to avoid narrow or tiny clusters.
**Bias**  | Values closer to `0` bias towards the X-axis, and values closer to `100` bias towards the Y-axis. A value of `50` will produce a even bias betwee both axes.
**Edge**  | Adjusts the edge between clusters. If `0`, there is no edge.
**Seed**  | Global seed


## Mode

<!-- SAMPLE treemap mode 3 -->
<table>
	<tr>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/treemap_mode0_compressed.jpg" alt="Example of a 'Mode' value of 0"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/treemap_mode1_compressed.jpg" alt="Example of a 'Mode' value of 1"></td>
		<td width="33.33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.2/treemap_mode2_compressed.jpg" alt="Example of a 'Mode' value of 2"></td>
	</tr>
	<tr>
		<th>Mode: <code>0</code></th>
		<th>Mode: <code>1</code></th>
		<th>Mode: <code>2</code></th>
	</tr>
	<tr>
		<td valign="top">Clusters height and colors are generated at random</td>
		<td valign="top">Clusters height and colors are based on the cluster area</td>
		<td valign="top">Same as mode <code>1</code> but in reverse</td>
	</tr>
</table>
<!-- END -->
