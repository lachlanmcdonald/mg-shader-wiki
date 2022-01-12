<!-- TOC -->
- [Brush Shaders](#brush-shaders)
- [Primitive Brush Shaders](#primitive-brush-shaders)
- [Volume Shaders](#volume-shaders)
- [Notes](#notes)

## Brush Shaders

> See: [How to use Brush Shaders](brush-shaders)

<!-- LIST list_brushes 140 -->
<table>
	<tr>
		<td valign="center" align="left"><a href="Brick-Brushes"><img width="140" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/bricks.png?cache=203" alt=""></a></td>
		<th valign="center" align="left"><a href="Brick-Brushes">Brick Brushes</a></th>
		<td valign="center">Generates alternating rows of bricks or tiles</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Noise-Brushes"><img width="140" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/cellular2D.png?cache=203" alt=""></a></td>
		<th valign="center" align="left"><a href="Noise-Brushes">Noise Brushes</a></th>
		<td valign="center">Generates different types of noise</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Gradient-Brush"><img width="140" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/gradient.png?cache=203" alt=""></a></td>
		<th valign="center" align="left"><a href="Gradient-Brush">Gradient Brush</a></th>
		<td valign="center">Generates different styles of gradients</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Radial-Gradient-Brush"><img width="140" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/gradient_radial.png?cache=203" alt=""></a></td>
		<th valign="center" align="left"><a href="Radial-Gradient-Brush">Radial Gradient Brush</a></th>
		<td valign="center">Generates different styles of radial gradients</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Grass-Brush"><img width="140" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/grass.png?cache=203" alt=""></a></td>
		<th valign="center" align="left"><a href="Grass-Brush">Grass Brush</a></th>
		<td valign="center">Generates generates randomly protruding lines of voxels with a constant distribution</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Grid-Brush"><img width="140" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/grid.png?cache=203" alt=""></a></td>
		<th valign="center" align="left"><a href="Grid-Brush">Grid Brush</a></th>
		<td valign="center">Generates a grid pattern with variable thickness and spacing</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Tiles-Brush"><img width="140" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/tiles.png?cache=203" alt=""></a></td>
		<th valign="center" align="left"><a href="Tiles-Brush">Tiles Brush</a></th>
		<td valign="center">Generates a tile pattern</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Puzzle-Tiles-Brush"><img width="140" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/tiles_puzzle.png?cache=203" alt=""></a></td>
		<th valign="center" align="left"><a href="Puzzle-Tiles-Brush">Puzzle Tile Brush</a></th>
		<td valign="center">Generates a puzzle tile pattern</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Uneven-Tiles-Brush"><img width="140" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/tiles_uneven.png?cache=203" alt=""></a></td>
		<th valign="center" align="left"><a href="Uneven-Tiles-Brush">Uneven Tile Brush</a></th>
		<td valign="center">Generates an uneven tile pattern</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Diagonal-Line-Brush"><img width="140" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/diagonal3.png?cache=203" alt=""></a></td>
		<th valign="center" align="left"><a href="Diagonal-Line-Brush">Diagonal Line Brush</a></th>
		<td valign="center">Generates parallel 45° lines of alternating widths and colors</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Weave-Brush"><img width="140" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/weave.png?cache=203" alt=""></a></td>
		<th valign="center" align="left"><a href="Weave-Brush">Weave Brush</a></th>
		<td valign="center">Generates a weave pattern</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Zigzag-Brushes"><img width="140" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/zigzag2.png?cache=203" alt=""></a></td>
		<th valign="center" align="left"><a href="Zigzag-Brushes">Zigzag Brushes</a></th>
		<td valign="center">Generates zig-zag patterns</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Truchet-Brush"><img width="140" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/truchet.png?cache=203" alt=""></a></td>
		<th valign="center" align="left"><a href="Truchet-Brush">Truchet Brush</a></th>
		<td valign="center">Generates a truchet pattern</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Treemap-Brush"><img width="140" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/treemap.png?cache=203" alt=""></a></td>
		<th valign="center" align="left"><a href="Treemap-Brush">Treemap Brush</a></th>
		<td valign="center">Generates a treemap pattern</td>
	</tr>
</table>
<!-- END -->

## Primitive Brush Shaders

> See: [How to use Brush Shaders](brush-shaders)

<!-- LIST list_primitives 140 -->
<table>
	<tr>
		<td valign="center" align="left"><a href="Prism-Brush"><img width="140" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/prism.png?cache=202" alt=""></a></td>
		<th valign="center" align="left"><a href="Prism-Brush">Prism Brush</a></th>
		<td valign="center">Generates prisms, pyramids or tetrahedrons with straight or curved angles</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Cylinder-Brush"><img width="140" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/cylinder.png?cache=202" alt=""></a></td>
		<th valign="center" align="left"><a href="Cylinder-Brush">Cylinder Brush</a></th>
		<td valign="center">Generates cylinders and tubes</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Stairs-Brushes"><img width="140" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/stairs.png?cache=202" alt=""></a></td>
		<th valign="center" align="left"><a href="Stairs-Brushes">Stairs Brushes</a></th>
		<td valign="center">Generates a slope of stairs</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Greeble-Brushes"><img width="140" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/greebles.png?cache=202" alt=""></a></td>
		<th valign="center" align="left"><a href="Greeble-Brushes">Greeble Brushes</a></th>
		<td valign="center">Generates greebles</td>
	</tr>
</table>
<!-- END -->

## Volume Shaders
- [How to use Volume Shaders](volume-shaders)

<!-- LIST list_volumes 140 -->
<table>
	<tr>
		<td valign="center" align="left"><a href="Heightmap"><img width="140" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/heightmap.png" alt=""></a></td>
		<th valign="center" align="left"><a href="Heightmap">Height-map</a></th>
		<td valign="center">Transforms a 2D height-map texture into a 3D volume</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Erode"><img width="140" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/erode.png" alt=""></a></td>
		<th valign="center" align="left"><a href="Erode">Erode</a></th>
		<td valign="center">Erodes selected colors using a noise texture</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Grass-Fit"><img width="140" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/grass_fit.png" alt=""></a></td>
		<th valign="center" align="left"><a href="Grass-Fit">Grass Fit</a></th>
		<td valign="center">Generates generates randomly protruding lines of voxels with a constant distribution</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="slices"><img width="140" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/slice.png" alt=""></a></td>
		<th valign="center" align="left"><a href="slices">Slices</a></th>
		<td valign="center">Removes a segment of the volume and shuffles voxels to fill its place</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="case"><img width="140" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/case.png" alt=""></a></td>
		<th valign="center" align="left"><a href="case">Case</a></th>
		<td valign="center">Surrounds/encases voxels</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="pyramid"><img width="140" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/pyramid.png" alt=""></a></td>
		<th valign="center" align="left"><a href="pyramid">Pyramid</a></th>
		<td valign="center">Iteratively generate a pyramid</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="sand"><img width="140" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/sand.png" alt=""></a></td>
		<th valign="center" align="left"><a href="sand">Sand</a></th>
		<td valign="center">Iteratively generate jagged voxels; i.e. piles of sand or cliffs</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="outline"><img width="140" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/outline.png" alt=""></a></td>
		<th valign="center" align="left"><a href="outline">Outline</a></th>
		<td valign="center">Creates an outline where voxels meet a voxel of a different color</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Soil-&-Cover"><img width="140" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/soil.png" alt=""></a></td>
		<th valign="center" align="left"><a href="Soil-&-Cover">Soil &amp; Cover</a></th>
		<td valign="center">Generates voxels above other voxels; i.e. snow or grass</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="noise"><img width="140" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/noise.png" alt=""></a></td>
		<th valign="center" align="left"><a href="noise">Noise</a></th>
		<td valign="center">Randomly generates noise of a specified size within a range of colors</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="random"><img width="140" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/random.png" alt=""></a></td>
		<th valign="center" align="left"><a href="random">Random</a></th>
		<td valign="center">Randomly generates noise with a set threshold</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="flood"><img width="140" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/flood.png" alt=""></a></td>
		<th valign="center" align="left"><a href="flood">Flood</a></th>
		<td valign="center">Generates a flood effect</td>
	</tr>
</table>
<!-- END -->

## Notes

- [Shaders in MagicaVoxel](Shaders-in-MagicaVoxel)
- [Terms](terms)
- [Commands](Commands)
