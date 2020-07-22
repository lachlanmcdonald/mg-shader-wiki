> **Brush Shaders** are shaders that allow you to easily to add or remove voxels from your geometry by selecting the area in which you want the shaders to take effect.

<!-- TOC -->
- [How to use a Brush Shader](#how-to-use-a-brush-shader)
- [List of shaders](#list-of-shaders)
  - [Brush Shaders](#brush-shaders)
  - [Primitive Brush Shaders](#primitive-brush-shaders)

## How to use a Brush Shader

1. Select **Box Mode** [B]
2. Select 
    - **Attach**: shader will only add new voxels
    - **Erase**: shader will only erase existing voxels
    - **Paint**: shader will only change existing voxels, but voxels will not be added or erased
    - **Marquee Select**: shader will create a selection of the existing voxels
3. Under Box, press the **Voxel Shader** option and **Gizmo**
4. Select the shader in the **Shader List**

<img src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/brush_shader.png" width="400" alt="">

_Relevant buttons in the editor UI._

<img src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/brush_shader_gizmo.png" width="400" alt="">

_Example of the box gizmo and the [brick brush shader](/lachlanmcdonald/magicavoxel-shaders/wiki/Brick-Brushes)._

## List of shaders

### Brush Shaders

<!-- LIST list_brushes 80 -->
<table>
	<tr>
		<td valign="center" align="left"><a href="Brick-Brushes"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/bricks.png?cache=1594482465" alt=""></a></td>
		<th valign="center" align="left"><a href="Brick-Brushes">Brick Brushes</a></th>
		<td valign="center">Generates alternating rows of bricks or tiles</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Grass-Brushes"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/grass.png?cache=1594482465" alt=""></a></td>
		<th valign="center" align="left"><a href="Grass-Brushes">Grass Brushes</a></th>
		<td valign="center">Generates generates randomly protruding lines of voxels with a constant distribution</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Grid-Brush"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/grid.png?cache=1594482465" alt=""></a></td>
		<th valign="center" align="left"><a href="Grid-Brush">Grid Brush</a></th>
		<td valign="center">Generates a grid pattern with variable thickness and spacing</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Tiles-Brush"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/tiles.png?cache=1594482465" alt=""></a></td>
		<th valign="center" align="left"><a href="Tiles-Brush">Tiles Brush</a></th>
		<td valign="center">Generates a tile pattern</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Puzzle-Tiles-Brush"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/tiles_puzzle.png?cache=1594482465" alt=""></a></td>
		<th valign="center" align="left"><a href="Puzzle-Tiles-Brush">Puzzle Tile Brush</a></th>
		<td valign="center">Generates a puzzle tile pattern</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Diagonal-Line-Brushes"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/diagonal2.png?cache=1594482465" alt=""></a></td>
		<th valign="center" align="left"><a href="Diagonal-Line-Brushes">Diagonal Line Brushes</a></th>
		<td valign="center">Generates parallel 45° lines of alternating widths</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Weave-Brush"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/weave.png?cache=1594482465" alt=""></a></td>
		<th valign="center" align="left"><a href="Weave-Brush">Weave Brush</a></th>
		<td valign="center">Generates a weave pattern</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Zigzag-Brushes"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/zigzag2.png?cache=1594482465" alt=""></a></td>
		<th valign="center" align="left"><a href="Zigzag-Brushes">Zigzag Brushes</a></th>
		<td valign="center">Generates zig-zag patterns</td>
	</tr>
</table>
<!-- END -->

### Primitive Brush Shaders

<!-- LIST list_primitives 80 -->
<table>
	<tr>
		<td valign="center" align="left"><a href="Prism-Brush"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/prism.png?cache=1594482465" alt=""></a></td>
		<th valign="center" align="left"><a href="Prism-Brush">Prism Brush</a></th>
		<td valign="center">Generates prisms, pyramids or tetrahedrons with straight or curved angles</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Cylinder-Brush"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/cylinder.png?cache=1594482465" alt=""></a></td>
		<th valign="center" align="left"><a href="Cylinder-Brush">Cylinder Brush</a></th>
		<td valign="center">Generates cylinders and tubes</td>
	</tr>
	<tr>
		<td valign="center" align="left"><a href="Stairs-Brushes"><img width="80" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/icons1/stairs.png?cache=1594482465" alt=""></a></td>
		<th valign="center" align="left"><a href="Stairs-Brushes">Stairs Brushes</a></th>
		<td valign="center">Generates a slope of stairs</td>
	</tr>
</table>
<!-- END -->
