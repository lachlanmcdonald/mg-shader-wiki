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

Setting **Color A** or **Color B** to `0` will result in no voxels being placed for those tiles, instead of a color.

## Example

<table>
    <tr>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/tiles.png" alt="Example"></td>
        <td width="50%"></td>
    </tr>
</table>
