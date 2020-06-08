> Generates a tile pattern. This shader is used as a [brush](Brush-Shaders).

## Parameters

- **Color A**: Tile color
- **Color B**: Alternate tile color
- **Width**: Width of the tile
- **Height**: Height of the tile
- **Depth**: Depth of the tile
- **X Offset**: Offset of the tiles in the X-axis
- **Y Offset**: Offset of the tiles in the Y-axis
- **Z Offset**: Offset of the tiles in the Z-axis

Setting **Color A** or **Color B** to `0` will result in no voxels being placed for that tile, instead of a color.