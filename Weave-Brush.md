> The **Weave [brush](Brush-Shaders)** generates a weave pattern.

- [Parameters](#parameters)
- [Color Mode](#color-mode)

## Parameters

- **Mode**: Color mode (see below)
- **Size**: Size of the squares
- **Color A**: Color A
- **Color B**: Color B
- **Line Color**: Color of the outline between squares
- **Line Width**: Width of the outline between squares

Setting any of the colors to `0` will also result in missing voxels.

## Color Mode

**Mode** determines how the pattern is coloured.

- **`0`**: Squares are colored at random between _Color A_ and _Color B._
- **`1`**: Squares alternate between _Color A_ and _Color B._
