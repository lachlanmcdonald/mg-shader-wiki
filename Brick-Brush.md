> The **Brick** [brush](Brush-Shaders) generates alternating rows of bricks or tiles.

- [Parameters](#parameters)
- [Threshold](#threshold)
- [Examples](#examples)

## Parameters

- **Width**: Width of the brick
- **Height**: Height of each brick
- **Depth**: Depth of each brick
- **Color A**: First color index
- **Color B**: Last color index
- **Threshold**: Likelihood of a brick being placed. The default of `1.0` means all bricks are placed, and lower values will result in missing bricks

Brick colors are chosen at random between __Color A__ and __Color B__.

Setting either of the colors to `0` will also result in missing bricks.


## Threshold

<table>
    <tr>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/5efad020-561b-4086-866d-40868862311e/bricks_threshold_1.png" alt="Example 1"></td>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/5efad020-561b-4086-866d-40868862311e/bricks_threshold_2.png" alt="Example 2"></td>
    </tr>
    <tr>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/5efad020-561b-4086-866d-40868862311e/bricks_threshold_3.png" alt="Example 3"></td>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/5efad020-561b-4086-866d-40868862311e/bricks_threshold_4.png" alt="Example 4"></td>
    </tr>
</table>

## Examples

<table>
    <tr>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/5efad020-561b-4086-866d-40868862311e/bricks_examples_1.png" alt="Example 1"></td>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/5efad020-561b-4086-866d-40868862311e/bricks_examples_2.png" alt="Example 2"></td>
    </tr>
    <tr>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/5efad020-561b-4086-866d-40868862311e/bricks_examples_3.png" alt="Example 3"></td>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/5efad020-561b-4086-866d-40868862311e/bricks_examples_4.png" alt="Example 4"></td>
    </tr>
</table>
