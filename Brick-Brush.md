Generates a brick or tile pattern. This shader is used as a [brush](#).

### Parameters

Brick colors are chosen at random between __Color A__ and __Color B__.

Setting either of the colors to zero will also result in missing bricks.

- **Width**: Width of the brick
- **Height**: Height of each brick
- **Depth**: Depth of each brick
- **Color A**: First color index
- **Color B**: Last color index
- **Threshold**: Likelihood of a brick being placed. The default of `1.0` means all bricks are placed, and lower values will result in missing bricks