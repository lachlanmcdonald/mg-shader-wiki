> **Brush Shaders** are shaders that allow you to easily to add or remove voxels from your geometry by selecting the area in which you want the shaders to take effect.

<!-- TOC -->
- [How to use a Brush Shader](#how-to-use-a-brush-shader)
- [Restricting voxels (painting existing voxels)](#restricting-voxels-painting-existing-voxels)
- [List of shaders](#list-of-shaders)
  - [Brush Shaders](#brush-shaders)
  - [Primitive Brush Shaders](#primitive-brush-shaders)

## How to use a Brush Shader

1. Select **Voxel Shader Mode** [C]
2. Select either:
    - **Attach**: to only add new voxels
    - **Erase**: to only erase existing voxels
    - **Paint**: to only change existing voxels (voxels will not be added or erased)
3. Select the shader in the **Shader List**

<table>
	<tr>
		<td valign="top"><img src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/ui/mv_ui1.png" width="130" alt=""></td>
		<td valign="top"><img src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/ui/mv_ui2.png" width="180" alt=""></td>
	</tr>
</table>

## Restricting voxels (painting existing voxels)

By default, [Brush Shaders](Brush-Shaders) are used with the **Voxel Shader Mode**, however, the **Paint** mode can also be used to replace voxels with the chosen color.

1. Right-click your chosen color and select **Inverse**
2. Right-click any other color and select **Voxel Selection by Color**
2. Select **Voxel Shader Mode** [C]
3. Select **Paint**
5. Select the shader in the **Shader List**
6. Draw a box over the volume; only the selected voxels will be updated.

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
		<td valign="center" align="left"><a href="Brick-Brushes"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/bricks.png?cache=201" alt=""></a></td>
		<th valign="center" align="left"><a href="Brick-Brushes">Brick Brushes</a></th>
		<td valign="center">Generates alternating rows of bricks or tiles</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Grass-Brush"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/grass.png?cache=201" alt=""></a></td>
		<th valign="center" align="left"><a href="Grass-Brush">Grass Brush</a></th>
		<td valign="center">Generates generates randomly protruding lines of voxels with a constant distribution</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Grid-Brush"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/grid.png?cache=201" alt=""></a></td>
		<th valign="center" align="left"><a href="Grid-Brush">Grid Brush</a></th>
		<td valign="center">Generates a grid pattern with variable thickness and spacing</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Tiles-Brush"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/tiles.png?cache=201" alt=""></a></td>
		<th valign="center" align="left"><a href="Tiles-Brush">Tiles Brush</a></th>
		<td valign="center">Generates a tile pattern</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Puzzle-Tiles-Brush"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/tiles_puzzle.png?cache=201" alt=""></a></td>
		<th valign="center" align="left"><a href="Puzzle-Tiles-Brush">Puzzle Tile Brush</a></th>
		<td valign="center">Generates a puzzle tile pattern</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Uneven-Tiles-Brush"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/tiles_uneven.png?cache=201" alt=""></a></td>
		<th valign="center" align="left"><a href="Uneven-Tiles-Brush">Uneven Tile Brush</a></th>
		<td valign="center">Generates an uneven tile pattern</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Diagonal-Line-Brush"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/diagonal3.png?cache=201" alt=""></a></td>
		<th valign="center" align="left"><a href="Diagonal-Line-Brush">Diagonal Line Brush</a></th>
		<td valign="center">Generates parallel 45° lines of alternating widths and colors</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Weave-Brush"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/weave.png?cache=201" alt=""></a></td>
		<th valign="center" align="left"><a href="Weave-Brush">Weave Brush</a></th>
		<td valign="center">Generates a weave pattern</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Zigzag-Brushes"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/zigzag2.png?cache=201" alt=""></a></td>
		<th valign="center" align="left"><a href="Zigzag-Brushes">Zigzag Brushes</a></th>
		<td valign="center">Generates zig-zag patterns</td>
	</tr>
</table>
<!-- END -->

### Primitive Brush Shaders

<!-- LIST list_primitives 80 -->
<table>
	<tr>
		<td valign="center" align="left"><a href="Prism-Brush"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/prism.png?cache=201" alt=""></a></td>
		<th valign="center" align="left"><a href="Prism-Brush">Prism Brush</a></th>
		<td valign="center">Generates prisms, pyramids or tetrahedrons with straight or curved angles</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Cylinder-Brush"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/cylinder.png?cache=201" alt=""></a></td>
		<th valign="center" align="left"><a href="Cylinder-Brush">Cylinder Brush</a></th>
		<td valign="center">Generates cylinders and tubes</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Stairs-Brushes"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/stairs.png?cache=201" alt=""></a></td>
		<th valign="center" align="left"><a href="Stairs-Brushes">Stairs Brushes</a></th>
		<td valign="center">Generates a slope of stairs</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Greeble-Brushes"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/greebles.png?cache=201" alt=""></a></td>
		<th valign="center" align="left"><a href="Greeble-Brushes">Greeble Brushes</a></th>
		<td valign="center">Generates greebles</td>
	</tr>
</table>
<!-- END -->
