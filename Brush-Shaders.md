> **Brush Shaders** are shaders that allow you to easily to add or remove voxels from the volume by selecting the area in which you want the shaders to take effect.

<!-- TOC -->
- [How to use a Brush Shader](#how-to-use-a-brush-shader)
- [Restricting voxels (painting existing voxels)](#restricting-voxels-painting-existing-voxels)
- [List of shaders](#list-of-shaders)
  - [Brush Shaders](#brush-shaders)
  - [Primitive Brush Shaders](#primitive-brush-shaders)

## How to use a Brush Shader

1. Select **Voxel Shader Mode** [C]
2. Select either:
    - **Attach**: to add new voxels (existing voxels are not removed)
    - **Erase**: to erase existing voxels (new voxels are not added)
    - **Paint**: to change existing voxels (voxels will not be added or removed)
3. Select the shader in the **Shader List**

<table>
	<tr>
		<td valign="top"><img src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/ui/mv_ui1.png" width="130" alt=""></td>
		<td valign="top"><img src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/ui/mv_ui2.png" width="180" alt=""></td>
	</tr>
</table>

## Restricting voxels (painting existing voxels)

By default, [Brush Shaders](Brush-Shaders) are used with the **Voxel Shader Mode** as shown above.

However, the **Paint** mode can also be used to replace only selected voxels. For example, to apply the [brick pattern](Brick-Brushes) to existing volumes.

1. Right-click the chosen color and select **Inverse**
2. Right-click any of the selected colors and select **Voxel Selection by Color**
3. Select **Voxel Shader Mode** [C]
4. Select **Paint**
5. Select the shader in the **Shader List**
6. Draw a box over the volume — only the selected voxels will be updated.

<table>
	<tr>
		<td valign="top"><img src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/ui/mv_ui3.png" width="130" alt=""></td>
		<td valign="top"><img src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/ui/mv_ui4.png" width="400" alt=""></td>
	</tr>
</table>

<table>
	<tr>
		<td><img src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/ui/mv_sel1.png" alt=""></td>
		<td><img src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/ui/mv_sel2.png" alt=""></td>
		<td><img src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/ui/mv_sel3.png" alt=""></td>
	</tr>
</table>

## List of shaders

### Brush Shaders

<!-- LIST list_brushes 80 -->
<table>
	<tr>
		<td valign="center" align="left"><a href="Brick-Brushes"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/bricks.png?cache=203" alt=""></a></td>
		<th valign="center" align="left"><a href="Brick-Brushes">Brick Brushes</a></th>
		<td valign="center">Generates alternating rows of bricks or tiles</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Noise-Brushes"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/cellular2D.png?cache=203" alt=""></a></td>
		<th valign="center" align="left"><a href="Noise-Brushes">Noise Brushes</a></th>
		<td valign="center">Generates different types of noise</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Gradient-Brush"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/gradient.png?cache=203" alt=""></a></td>
		<th valign="center" align="left"><a href="Gradient-Brush">Gradient Brush</a></th>
		<td valign="center">Generates different styles of gradients</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Radial-Gradient-Brush"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/gradient_radial.png?cache=203" alt=""></a></td>
		<th valign="center" align="left"><a href="Radial-Gradient-Brush">Radial Gradient Brush</a></th>
		<td valign="center">Generates different styles of radial gradients</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Grass-Brush"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/grass.png?cache=203" alt=""></a></td>
		<th valign="center" align="left"><a href="Grass-Brush">Grass Brush</a></th>
		<td valign="center">Generates generates randomly protruding lines of voxels with a constant distribution</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Grid-Brush"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/grid.png?cache=203" alt=""></a></td>
		<th valign="center" align="left"><a href="Grid-Brush">Grid Brush</a></th>
		<td valign="center">Generates a grid pattern with variable thickness and spacing</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Tiles-Brush"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/tiles.png?cache=203" alt=""></a></td>
		<th valign="center" align="left"><a href="Tiles-Brush">Tiles Brush</a></th>
		<td valign="center">Generates a tile pattern</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Puzzle-Tiles-Brush"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/tiles_puzzle.png?cache=203" alt=""></a></td>
		<th valign="center" align="left"><a href="Puzzle-Tiles-Brush">Puzzle Tile Brush</a></th>
		<td valign="center">Generates a puzzle tile pattern</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Uneven-Tiles-Brush"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/tiles_uneven.png?cache=203" alt=""></a></td>
		<th valign="center" align="left"><a href="Uneven-Tiles-Brush">Uneven Tile Brush</a></th>
		<td valign="center">Generates an uneven tile pattern</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Diagonal-Line-Brush"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/diagonal3.png?cache=203" alt=""></a></td>
		<th valign="center" align="left"><a href="Diagonal-Line-Brush">Diagonal Line Brush</a></th>
		<td valign="center">Generates parallel 45° lines of alternating widths and colors</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Weave-Brush"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/weave.png?cache=203" alt=""></a></td>
		<th valign="center" align="left"><a href="Weave-Brush">Weave Brush</a></th>
		<td valign="center">Generates a weave pattern</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Zigzag-Brushes"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/zigzag2.png?cache=203" alt=""></a></td>
		<th valign="center" align="left"><a href="Zigzag-Brushes">Zigzag Brushes</a></th>
		<td valign="center">Generates zig-zag patterns</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Truchet-Brush"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/truchet.png?cache=203" alt=""></a></td>
		<th valign="center" align="left"><a href="Truchet-Brush">Truchet Brush</a></th>
		<td valign="center">Generates a truchet pattern</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Treemap-Brush"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons2/treemap.png?cache=203" alt=""></a></td>
		<th valign="center" align="left"><a href="Treemap-Brush">Treemap Brush</a></th>
		<td valign="center">Generates a treemap pattern</td>
	</tr>
</table>
<!-- END -->

### Primitive Brush Shaders

<!-- LIST list_primitives 80 -->
<table>
	<tr>
		<td valign="center" align="left"><a href="Prism-Brush"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/prism.png?cache=202" alt=""></a></td>
		<th valign="center" align="left"><a href="Prism-Brush">Prism Brush</a></th>
		<td valign="center">Generates prisms, pyramids or tetrahedrons with straight or curved angles</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Cylinder-Brush"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/cylinder.png?cache=202" alt=""></a></td>
		<th valign="center" align="left"><a href="Cylinder-Brush">Cylinder Brush</a></th>
		<td valign="center">Generates cylinders and tubes</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Stairs-Brushes"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/stairs.png?cache=202" alt=""></a></td>
		<th valign="center" align="left"><a href="Stairs-Brushes">Stairs Brushes</a></th>
		<td valign="center">Generates a slope of stairs</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Greeble-Brushes"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/greebles.png?cache=202" alt=""></a></td>
		<th valign="center" align="left"><a href="Greeble-Brushes">Greeble Brushes</a></th>
		<td valign="center">Generates greebles</td>
	</tr>
</table>
<!-- END -->
