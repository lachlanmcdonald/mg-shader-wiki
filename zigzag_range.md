> **zigzag_range** is a **[Zigzag brush](Zigzag-Brushes)** that generates zigzag patterns between a range of colors; with a line for each color in the range.

- [Parameters](#parameters)
- [Direction](#direction)
- [Examples](#examples)

## Parameters

- **Direction**: Direction of the pattern (see below)
- **Width**: Width of the lines
- **Color A**: First color index
- **Color B**: Last color index

Setting either of the colors to `0` will result in empty voxels.

## Direction

<table>
    <tr>
        <td width="50%"><img src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.4/zigzag_range_direction0.png" alt="Example of a direction of 0"></td>
        <td width="50%"><img src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.4/zigzag_range_direction1.png" alt="Example of a direction of 1"></td>
    </tr>
    <tr>
        <th>Direction: <code>0</code></th>
        <th>Direction: <code>1</code></th>
    </tr>
    <tr>
        <td width="50%"><img src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.4/zigzag_range_direction2.png" alt="Example of a direction of 2"></td>
        <td width="50%"><img src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.4/zigzag_range_direction3.png" alt="Example of a direction of 3"></td>
    </tr>
    <tr>
        <th>Direction: <code>2</code></th>
        <th>Direction: <code>3</code></th>
    </tr>
</table>

## Examples

<table>
    <tr>
        <td width="33%"><img src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.2/zigzag_range_example0.png" alt="Example"></td>
        <td width="33%"><img src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.2/zigzag_range_example1.png" alt="Example"></td>
        <td width="33%"><img src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.2/zigzag_range_example2.png" alt="Example"></td>
    </tr>
</table>
