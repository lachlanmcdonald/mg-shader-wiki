> **Volume Shaders** are shaders that apply to the entire volume.

<!-- TOC -->
- [How to use a Brush Shader](#how-to-use-a-brush-shader)
- [List of shaders](#list-of-shaders)

## How to use a Brush Shader

1. Select the shader in the **Shader List**
2. Adjust the parameters and press the **Execute Shader** button
3. If you want to adjust the results, **undo**, adjust and re-execute 

Some shaders, like [Pyramid](pyramid) and [Sand](sand), add voxels layer-by-later; so you should execute these as many times as you like until the desired effect is attained.


## List of shaders

<!-- LIST list_volumes 120 -->
<table>
	<tr>
		<td valign="center" align="left"><a href="Heightmap"><img width="120" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/heightmap.png" alt=""></a></td>
		<th valign="center" align="left"><a href="Heightmap">Heightmap</a></th>
		<td valign="center">Transforms a 2D height-map texture into a 3D volume</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Erode"><img width="120" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/erode.png" alt=""></a></td>
		<th valign="center" align="left"><a href="Erode">Erode</a></th>
		<td valign="center">Erodes selected colors using a noise texture</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Grass-Fit"><img width="120" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/grass_fit.png" alt=""></a></td>
		<th valign="center" align="left"><a href="Grass-Fit">Grass Fit</a></th>
		<td valign="center">Generates generates randomly protruding lines of voxels with a constant distribution</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="slices"><img width="120" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/slice.png" alt=""></a></td>
		<th valign="center" align="left"><a href="slices">Slices</a></th>
		<td valign="center">Removes a segment of the volume and shuffles voxels to fill its place</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="case"><img width="120" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/case.png" alt=""></a></td>
		<th valign="center" align="left"><a href="case">Case</a></th>
		<td valign="center">Surrounds/encases voxels</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="pyramid"><img width="120" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/pyramid.png" alt=""></a></td>
		<th valign="center" align="left"><a href="pyramid">Pyramid</a></th>
		<td valign="center">Iteratively generate a pyramid</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="sand"><img width="120" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/sand.png" alt=""></a></td>
		<th valign="center" align="left"><a href="sand">Sand</a></th>
		<td valign="center">Iteratively generate jagged voxels; i.e. piles of sand or cliffs</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="outline"><img width="120" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/outline.png" alt=""></a></td>
		<th valign="center" align="left"><a href="outline">Outline</a></th>
		<td valign="center">Creates an outline where voxels meet a voxel of a different color</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Soil-&-Cover"><img width="120" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/soil.png" alt=""></a></td>
		<th valign="center" align="left"><a href="Soil-&-Cover">Soil &amp; Cover</a></th>
		<td valign="center">Generates voxels above other voxels; i.e. snow or grass</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="noise"><img width="120" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/noise.png" alt=""></a></td>
		<th valign="center" align="left"><a href="noise">Noise</a></th>
		<td valign="center">Randomly generates noise of a specified size within a range of colors</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="random"><img width="120" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/random.png" alt=""></a></td>
		<th valign="center" align="left"><a href="random">Random</a></th>
		<td valign="center">Randomly generates noise with a set threshold</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="flood"><img width="120" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/flood.png" alt=""></a></td>
		<th valign="center" align="left"><a href="flood">Flood</a></th>
		<td valign="center">Generates a flood effect</td>
	</tr>
</table>
<!-- END -->
