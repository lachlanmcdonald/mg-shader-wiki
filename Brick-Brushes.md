> The **Brick [brushes](Brush-Shaders)** generates alternating rows of randomly colored bricks.
> 
> There are two shaders, **`bricks`** and **`bricks_vert`**, that are functionally identical except bricks are offset vertically for `bricks_vert` and horizontally for `bricks`.

<!-- TOC -->
- [Shaders](#shaders)
- [Parameters](#parameters)
- [Direction](#direction)
- [Threshold](#threshold)

## Shaders

<table>
    <tr>
        <td width="33%">
            <img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/3cf75dcc-5b1c-465b-81fc-8b4526c4363a/bricks_horz.png" alt="Example of the bricks shader">
        </td>
        <td width="33%">
            <img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/3cf75dcc-5b1c-465b-81fc-8b4526c4363a/bricks_vert.png" alt="Example of the bricks_vert shader">
        </td>
    </tr>
    <tr>
        <th><code>bricks</code></th>
        <th><code>bricks_vert</code></th>
    </tr>
</table>

## Parameters

Parameter | Description
--------- | -----------
**Direction** | Facing direction of the bricks
**Width** | Width of the brick
**Height** | Height of each brick
**Depth** | Depth of each brick
**Offset** | Misalignment of bricks per row (a value of `0` will determine the misalignment automatically)
**Color A** | First color index
**Color B** | Last color index
**Threshold** | Likelihood of a brick being placed. The default of `1.0` means all bricks are placed, and lower values will result in missing bricks

Brick colors are chosen at random between __Color A__ and __Color B__. Setting either of the colors to `0` will also result in missing bricks.

## Direction

<table>
    <tr>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/3cf75dcc-5b1c-465b-81fc-8b4526c4363a/bricks_direction_0.png" alt="Example of direction 0"></td>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/3cf75dcc-5b1c-465b-81fc-8b4526c4363a/bricks_direction_1.png" alt="Example of direction 1"></td>
    </tr>
    <tr>
        <th>Direction: <code>0</code></th>
        <th>Direction: <code>1</code></th>
    </tr>
    <tr>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/3cf75dcc-5b1c-465b-81fc-8b4526c4363a/bricks_direction_2.png" alt="Example of direction 2"></td>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/3cf75dcc-5b1c-465b-81fc-8b4526c4363a/bricks_direction_3.png" alt="Example of direction 3"></td>
    </tr>
    <tr>
        <th>Direction: <code>2</code></th>
        <th>Direction: <code>3</code></th>
    </tr>
</table>

## Threshold

<table>
    <tr>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/3cf75dcc-5b1c-465b-81fc-8b4526c4363a/bricks_threshold_10.png" alt="Example of a threshold of 1.0"></td>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/3cf75dcc-5b1c-465b-81fc-8b4526c4363a/bricks_threshold_08.png" alt="Example of a threshold of 0.8"></td>
    </tr>
    <tr>
        <th>Threshold: <code>1.0</code></th>
        <th>Threshold: <code>0.8</code></th>
    </tr>
    <tr>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/3cf75dcc-5b1c-465b-81fc-8b4526c4363a/bricks_threshold_06.png" alt="Example of a threshold of 0.6"></td>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/3cf75dcc-5b1c-465b-81fc-8b4526c4363a/bricks_threshold_04.png" alt="Example of a threshold of 0.4"></td>
    </tr>
    <tr>
        <th>Threshold: <code>0.6</code></th>
        <th>Threshold: <code>0.4</code></th>
    </tr>
</table>
