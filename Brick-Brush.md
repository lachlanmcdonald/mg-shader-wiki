> The **Brick** [brush](Brush-Shaders) generates alternating rows of randomly colored bricks or tiles.
> 
> There are two shaders, **bricks** and **bricks_vert**, which are functionally identical except bricks are offset vertically for **bricks_vert** and horizontally for **bricks**.

- [Parameters](#parameters)
- [Direction](#direction)
- [Threshold](#threshold)

<table>
    <tr>
        <td width="33%">
            <img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/3cf75dcc-5b1c-465b-81fc-8b4526c4363a/bricks_horz.png" alt="Example of the bricks shader">
            <code>bricks</code>
        </td>
        <td width="33%">
            <img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/3cf75dcc-5b1c-465b-81fc-8b4526c4363a/bricks_vert.png" alt="Example of the bricks_vert shader">
            <code>bricks_vert</code>
        </td>
        <td width="33%"></td>
    </tr>
</table>

## Parameters

- **Direction**: Facing direction of the bricks
- **Width**: Width of the brick
- **Height**: Height of each brick
- **Depth**: Depth of each brick
- **Offset**: Misalignment of bricks per row (a value of `0` will determine the misalignment automatically)
- **Color A**: First color index
- **Color B**: Last color index
- **Threshold**: Likelihood of a brick being placed. The default of `1.0` means all bricks are placed, and lower values will result in missing bricks

Brick colors are chosen at random between __Color A__ and __Color B__. Setting either of the colors to `0` will also result in missing bricks.

## Direction

<table>
    <tr>
        <td width="50%">
        <img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/3cf75dcc-5b1c-465b-81fc-8b4526c4363a/bricks_direction_0.png" alt="Example of direction 1">
        Direction: <code>0</code>
        </td>
        <td width="50%">
        <img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/3cf75dcc-5b1c-465b-81fc-8b4526c4363a/bricks_direction_1.png" alt="Example of direction 1">
        Direction: <code>1</code>
        </td>
    </tr>
    <tr>
        <td width="50%">
        <img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/3cf75dcc-5b1c-465b-81fc-8b4526c4363a/bricks_direction_2.png" alt="Example of direction 1">
        Direction: <code>2</code>
        </td>
        <td width="50%">
        <img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/3cf75dcc-5b1c-465b-81fc-8b4526c4363a/bricks_direction_3.png" alt="Example of direction 1">
        Direction: <code>3</code>
        </td>
    </tr>
</table>

## Threshold

<table>
    <tr>
        <td width="50%">
            <img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/3cf75dcc-5b1c-465b-81fc-8b4526c4363a/bricks_threshold_10.png" alt="Example of a threshold of 1.0">
            <code>1.0</code>
        </td>
        <td width="50%">
            <img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/3cf75dcc-5b1c-465b-81fc-8b4526c4363a/bricks_threshold_08.png" alt="Example of a threshold of 0.8">
            <code>0.8</code>
        </td>
    </tr>
    <tr>
        <td width="50%">
            <img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/3cf75dcc-5b1c-465b-81fc-8b4526c4363a/bricks_threshold_06.png" alt="Example of a threshold of 0.6">
            <code>0.6</code>
        </td>
        <td width="50%">
            <img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/3cf75dcc-5b1c-465b-81fc-8b4526c4363a/bricks_threshold_04.png" alt="Example of a threshold of 0.4">
            <code>0.4</code>
        </td>
    </tr>
</table>
