> **diagonal_range** is a **[Diagonal Line Brushes](Diagonal-Line-Brushes)** that generates diagonal patterns between a range of colors; with a line for each color in the range.

- [Parameters](#parameters)
- [Directions](#directions)

## Parameters

- **Direction**: Direction of the lines on the Z-axis (see below)
- **Color A**: First color index
- **Color B**: Last color index
- **Width**: Thickness of the lines
- **Offset**: Adjusts the offset of the lines

Setting either of the colors to `0` will result in empty voxels.

## Directions

<table>
    <tr>
        <td width="33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.4/diagonal_range_direction0.png" alt="Example of a direction of 0"></td>
        <td width="33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.4/diagonal_range_direction1.png" alt="Example of a direction of 1"></td>
        <td width="33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.4/diagonal_range_direction2.png" alt="Example of a direction of 2"></td>
    </tr>
    <tr>
        <th>Direction: <code>0</code></th>
        <th>Direction: <code>1</code></th>
        <th>Direction: <code>2</code></th>
    </tr>
    <tr>
        <td width="33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.4/diagonal_range_direction3.png" alt="Example of a direction of 3"></td>
        <td width="33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.4/diagonal_range_direction4.png" alt="Example of a direction of 4"></td>
        <td width="33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.10.4/diagonal_range_direction5.png" alt="Example of a direction of 5"></td>
    </tr>
    <tr>
        <th>Direction: <code>3</code></th>
        <th>Direction: <code>4</code></th>
        <th>Direction: <code>5</code></th>
    </tr>
</table>
