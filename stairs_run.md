> **stairs_runs** is a **[Stairs Brushes](Stairs-Brushes)** that generates only stair runs; with additional options for the size and spacing of the runs.

- [Parameters](#parameters)
- [Count](#count)
- [Height](#height)
- [X/Y Gap](#xy-gap)
- [Z Gap](#z-gap)

## Parameters

Parameter | Description
--------- | -----------
**Direction** | The facing direction of the stairs
**Count**     | The number of runs to fit within the brushes dimensions. If the box's dimensions are not divisible by the count, the depth of each run will be inconsistent
**Height**    | The height of each run
**X/Y Gap**   | The distance between each run of adjacent stairs
**Z Gap**     | The distance between each run and the next run above it (also known as the _rise._)

## Count

<table>
    <tr>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/stairs_count_2.png" alt="Example of a Count of 2"></td>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/stairs_count_4.png" alt="Example of a Count of 4"></td>
    </tr>
    <tr>
        <th>Count: <code>2</code></th>
        <th>Count: <code>4</code></th>
    </tr>
    <tr>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/stairs_count_6.png" alt="Example of a Count of 6"></td>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/stairs_count_8.png" alt="Example of a Count of 8"></td>
    </tr>
    <tr>
        <th>Count: <code>6</code></th>
        <th>Count: <code>8</code></th>
    </tr>
</table>

## Height

<table>
    <tr>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/stairs_height_1.png" alt="Example of a Height of 1"></td>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/stairs_height_2.png" alt="Example of a Height of 2"></td>
    </tr>
    <tr>
        <th>Height: <code>1</code></th>
        <th>Height: <code>2</code></th>
    </tr>
    <tr>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/stairs_height_3.png" alt="Example of a Height of 3"></td>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/stairs_height_4.png" alt="Example of a Height of 4"></td>
    </tr>
    <tr>
        <th>Height: <code>3</code></th>
        <th>Height: <code>4</code></th>
    </tr>
</table>

## X/Y Gap

<table>
    <tr>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/stairs_xy_gap_0.png" alt="Example of a X/Y Gap of 0"></td>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/stairs_xy_gap_1.png" alt="Example of a X/Y Gap of 1"></td>
    </tr>
    <tr>
        <th>X/Y Gap: <code>0</code></th>
        <th>X/Y Gap: <code>1</code></th>
    </tr>
    <tr>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/stairs_xy_gap_2.png" alt="Example of a X/Y Gap of 2"></td>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/stairs_xy_gap_3.png" alt="Example of a X/Y Gap of 3"></td>
    </tr>
    <tr>
        <th>X/Y Gap: <code>2</code></th>
        <th>X/Y Gap: <code>3</code></th>
    </tr>
</table>

## Z Gap

<table>
    <tr>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/stairs_z_gap_0.png" alt="Example of a Z Gap of 0"></td>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/stairs_z_gap_1.png" alt="Example of a Z Gap of 1"></td>
    </tr>
    <tr>
        <th>Z Gap: <code>0</code></th>
        <th>Z Gap: <code>1</code></th>
    </tr>
    <tr>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/stairs_z_gap_2.png" alt="Example of a Z Gap of 2"></td>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/stairs_z_gap_3.png" alt="Example of a Z Gap of 3"></td>
    </tr>
    <tr>
        <th>Z Gap: <code>2</code></th>
        <th>Z Gap: <code>3</code></th>
    </tr>
</table>
